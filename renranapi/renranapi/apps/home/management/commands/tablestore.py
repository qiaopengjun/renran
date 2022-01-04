from django.core.management import BaseCommand
from renranapi.utils.tablestore import *


class Command(BaseCommand):
    help = """表格存储命令必须接收而且只接收1个命令参数，如下：
    python manage.py tablestore create  表示创建项目使用的表格 
    python manage.py tablestore delete  表示删除项目使用的表格
    """

    def __init__(self, *args, **kwargs):
        self.client = OTS()
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        """参数设置"""
        parser.add_argument("argument", nargs="*", help="操作类型")  # 位置参数

    def handle(self, *args, **options):
        """
        表格存储的初始化
        :param args:
        :param options:  参数列表
        :return:
        """
        argument = options.get("argument")
        if len(argument) != 1:
            self.stderr.write("操作有误！")
            self.stdout.write(self.help)
            return None

        if argument[0] == "create":
            """创建表格"""
            self.create_table()

        elif argument[0] == "delete":
            """删除表格"""
            self.delete_table()
        else:
            self.stderr.write("操作有误！")
            self.stdout.write(self.help)

    def create_table(self):
        # 存储库[收件箱]
        table_name = "user_message_table"
        schema_of_primary_key = [  # 主键列
            ('id', 'INTEGER'),  # 分区键
            ('user_id', 'INTEGER'),
            ('sequence_id', 'INTEGER', PK_AUTO_INCR),
            ("message_id", 'INTEGER')
        ]
        self.stdout.write("表格《%s》创建开始..." % table_name)
        self.client.create_table(table_name, schema_of_primary_key)
        self.stdout.write("表格《%s》创建完成..." % table_name)

        # 关系库
        table_name = "user_relation_table"
        schema_of_primary_key = [  # 主键列
            ('id', 'INTEGER'),  # 分区键
            ('user_id', 'INTEGER'),
            ("follow_user_id", 'INTEGER'),
        ]

        self.stdout.write("表格《%s》创建开始..." % table_name)
        self.client.create_table(table_name, schema_of_primary_key)
        self.stdout.write("表格《%s》创建完成..." % table_name)

        # 未读池
        table_name = "user_message_session_table"
        # 主键列
        schema_of_primary_key = [
            ('id', 'INTEGER'),
            ('follow_user_id', 'INTEGER'),
            ("last_sequence_id", 'INTEGER'),
        ]

        self.stdout.write("表格《%s》创建开始..." % table_name)
        self.client.create_table(table_name, schema_of_primary_key)
        self.stdout.write("表格《%s》创建完成..." % table_name)

        # 推送日志
        table_name = "user_message_log_table"
        schema_of_primary_key = [  # 主键列
            ('id', 'INTEGER'),
            ('user_id', 'INTEGER'),
            ("message_id", 'INTEGER'),
        ]

        self.client.create_table(table_name, schema_of_primary_key)
        self.stdout.write("表格《%s》创建完成..." % table_name)

    def delete_table(self):
        """删除表操作"""
        table_list = OTS().list_table()
        for table_name in table_list:
            self.client.delete_table(table_name)
            self.stdout.write("表格《%s》删除完成..." % table_name)

        self.stdout.write("所有表格删除完成...")
