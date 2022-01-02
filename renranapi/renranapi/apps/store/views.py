from django.shortcuts import render
# from tablestore import OTSClient,TableMeta,TableOptions,ReservedThroughput,CapacityUnit,PK_AUTO_INCR
from tablestore import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

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
        ret = OTS().delete_table("user_message_session_table")
        print(ret)
        # 删除多张表
        ret = OTS().delete_table(["user_message_table", "user_relation_table"])
        print(ret)
        return Response("ok")
