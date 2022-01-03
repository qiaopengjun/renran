from django.shortcuts import render
# from tablestore import OTSClient,TableMeta,TableOptions,ReservedThroughput,CapacityUnit,PK_AUTO_INCR
from tablestore import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone as datetime

# Create your views here.
"""表格存储的基本入门代码"""
"""初始化tablestore sdk对象"""


class OTS(object):
    def __init__(self):
        self.client = OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def list_table(self):
        """列出所有的存储表"""
        return self.client.list_table()

    def create_table(self, table_name, schema_of_primary_key):
        """
        :param table_name: 字符串，表名
        :param schema_of_primary_key: 列表，每一个成员是一个元祖，表示字段的名称和类型
        :return:
        """
        # 通过表名和主键列的schema创建一个tableMeta。
        table_meta = TableMeta(table_name, schema_of_primary_key)
        # 创建TableOptions，数据保留31536000秒，超过后自动删除；最大3个版本；写入时指定的版本值和当前标准时间相差不能超过1天。
        table_options = TableOptions(31536000, 3, 86400)
        # 设置预留读吞吐量为0，预留写吞吐量为0。
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))

        try:
            self.client.create_table(table_meta, table_options, reserved_throughput)
            return True
        # 处理异常。
        except Exception:
            return False

    def delete_table(self, table_name):
        """
        删除表
        :param table_name: 参数如果是字符串，则表示删除一张表，
                           参数如果是列表，则表示删除多张表
        :return:
        """
        tables = []
        if type(table_name) is str:
            tables.append(table_name)
        else:
            tables = table_name

        ret = {
            "success": [],
            "fails": []
        }
        for table in tables:
            try:
                self.client.delete_table(table)
                ret["success"].append(table)
            except Exception:
                ret["fails"].append(table)

        return ret

    def put_row(self, table_name, primary_key, attribute_columns={}):
        """
        添加一条数据
        :param table_name: 本次添加数据的表名
        :param primary_key: 主键列
        :param attribute_columns: 其他属性列
        :return: 新增数据的主键
        """

        primary_key_list = []
        for key, value in primary_key.items():
            primary_key_list.append((key, value))

        attribute_columns_list = []
        for key, value in attribute_columns.items():
            attribute_columns_list.append((key, value))

        row = Row(primary_key_list, attribute_columns_list)
        # 添加数据的条件
        # EXPECT_NOT_EXIST 如果主键重复，则报错！
        condition = Condition(RowExistenceExpectation.EXPECT_NOT_EXIST)
        try:
            # 调用put_row方法, ReturnType.RT_PK表示返回新增数据的主键信息，如果不设置则返回None
            consumed, return_row = self.client.put_row(table_name, row, condition, ReturnType.RT_PK)
            return True, return_row.primary_key
        except OTSClientError as e:
            """网络异常"""
            return False, "put row failed, http_status:%d, error_message:%s" % (
                e.get_http_status(), e.get_error_message())

        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            """参数有误"""
            return False, "put row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
                e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id())
        except Exception as e:
            """其他错误"""
            return False, "未知的异常"

    def get_row(self, table_name, primary_key, columns_to_get=[], column_filter=None):
        """"""
        # 指定查询结果返回的属性列
        # 过滤条件
        """
        # ====================== 多条件 ========================
        # 逻辑条件
        cond = CompositeColumnCondition(LogicalOperator.AND)
        cond = CompositeColumnCondition(LogicalOperator.OR)
        cond = CompositeColumnCondition(LogicalOperator.NOT)
        # 比较条件
        ComparatorType.NOT_EQUAL  !=
        ComparatorType.EQUAL      ==
        GREATER_THAN              >
        GREATER_EQUAL             >=
        LESS_THAN                 <
        LESS_EQUAL                <=
        举例：
          查询一个学生信息，性别为男的，小于20岁===>   sex=男 and age < 20
            cond = CompositeColumnCondition(LogicalOperator.AND)
            cond.add_sub_condition(SingleColumnCondition("sex", '男', ComparatorType.EQUAL))
            cond.add_sub_condition(SingleColumnCondition("age", 20, ComparatorType.LESS_THAN))


        # ====================== 单条件 ======================== 
        cond = SingleColumnCondition("age", 20, ComparatorType.LESS_THAN)
        """
        primary_key_list = []
        for key, value in primary_key.items():
            primary_key_list.append((key, value))
        try:
            # 调用get_row接口查询
            consumed, return_row, next_token = self.client.get_row(table_name, primary_key_list, columns_to_get,
                                                                   column_filter, 1)
            data = {}
            for att in return_row.primary_key:
                # 打印每一个字段的内容
                data[att[0]] = att[1]
            if len(columns_to_get) > 0:
                """如果有指定要返回其他属性列"""
                for att in return_row.attribute_columns:
                    # 打印每一个字段的内容
                    data[att[0]] = att[1]
            return True, data
            # 客户端异常，一般为参数错误或者网络异常。
        except OTSClientError as e:
            return False, "获取数据失败, http_status:%d, error_message:%s" % (e.get_http_status(), e.get_error_message())
        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            return False, "获取数据失败, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
                e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id())
        except Exception as e:
            return False, "未知异常"

    def update_row(self, table_name, primary_key, attribute_columns):
        """更新一条数据"""
        primary_key_list = []
        for key, value in primary_key.items():
            primary_key_list.append((key, value))

        attribute_columns_list = []
        for key, value in attribute_columns.items():
            attribute_columns_list.append((key, value))

        update_of_attribute_columns = {
            'PUT': attribute_columns_list,
        }

        row = Row(primary_key_list, update_of_attribute_columns)

        try:
            consumed, return_row = self.client.update_row(table_name, row, condition=None, return_type=ReturnType.RT_PK)
            data = {}
            for att in return_row.primary_key:
                # 打印每一个字段的内容
                data[att[0]] = att[1]

            return True, data
        # 客户端异常，一般为参数错误或者网络异常。
        except OTSClientError as e:
            return False, "更新失败, http_status:%d, error_message:%s" % (e.get_http_status(), e.get_error_message())

        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            return False, "更新失败, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
                e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id())
        except Exception as e:
            return False, "未知异常"

    def delete_row(self, table_name, primary_key):
        """根据主键删除一条数据"""
        primary_key_list = []
        for key, value in primary_key.items():
            primary_key_list.append((key, value))
        row = Row(primary_key_list)
        try:
            consumed, return_row = self.client.delete_row(table_name, row, None)
            return True, "删除成功"
        except OTSClientError as e:
            return False, "更新失败！网络异常, http_status:%d, error_message:%s" % (e.get_http_status(), e.get_error_message())
        except OTSServiceError as e:
            return False, "更新失败，参数有误, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
                e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id())
        except Exception as e:
            return False, "未知异常"


class TableAPIView(APIView):

    def get(self, request):
        """获取当前仓库中所有的数据表"""
        tables = OTS().list_table()
        print(tables)
        return Response("ok")

    def post(self, request):
        OTS().create_table("user_relation_table", [
            ("user_id", "INTEGER"),
            ("follow_user_id", "INTEGER")
        ])

        OTS().create_table("user_message_table", [
            ("follow_user_id", "INTEGER"),
            ("sequence_id", "INTEGER", PK_AUTO_INCR),  # 设为自增字段
            ("user_id", "INTEGER"),
            ("message_id", "INTEGER"),
        ])

        OTS().create_table("user_message_session_table", [
            ("follow_user_id", "INTEGER"),
            ("last_sequence_id", "INTEGER"),
        ])
        return Response("ok")

    def delete(self, request):
        """删除指定的表"""
        # 删除一张表
        # ret = OTS().delete_table("user_message_session_table")
        # print(ret)
        # 删除多张表
        ret = OTS().delete_table(["user_message_table", "user_relation_table"])
        print(ret)
        return Response("ok")


class DataAPIView(APIView):
    def post(self, request):
        """添加一条数据"""
        # 主键 = {"主键名":"值","主键名":"值",,,}
        primary_key = {"user_id": 1, 'follow_user_id': 3}

        # 属性列 = {"字段名":"值"}
        attribute_columns = {'timestamp': datetime.now().timestamp()}

        ret = OTS().put_row("user_relation_table", primary_key, attribute_columns)

        print(ret[0])

        return Response("OK")

    def get(self, request):
        """获取一条数据"""
        primary_key = {"user_id": 1, 'follow_user_id': 3}
        ret = OTS().get_row("user_relation_table", primary_key, columns_to_get=["timestamp"])
        return Response(ret)

    def put(self, request):
        primary_key = {"user_id": 1, 'follow_user_id': 2}
        attribute_columns = {"timestamp": 1000888}
        ret = OTS().update_row("user_relation_table", primary_key, attribute_columns)
        return Response(ret)

    def delete(self, request):
        primary_key = {"user_id": 1, 'follow_user_id': 2}
        ret = OTS().delete_row("user_relation_table", primary_key)
        return Response(ret)
