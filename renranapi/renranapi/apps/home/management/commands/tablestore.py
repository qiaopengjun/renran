from django.core.management import BaseCommand


class Command(BaseCommand):
    help = """测试命令的帮助文档"""

    def add_arguments(self, parser):
        """参数设置"""
        parser.add_argument("argument", nargs="*", help="必填参数的说明")  # 位置参数
        parser.add_argument("--option", '-p', default=None, help="可选参数的说明")  # 选项参数

    def handle(self, *args, **options):
        """命令主方法
        options: 参数列表
        """
        argument = options.get("argument")  # 获取位置参数
        option = options.get("option")  # 获取选项参数

        self.stdout.write("argument: %s" % argument)
        self.stdout.write("option: %s" % option)

        if option is None:
            self.stdout.write("没有设置option选项参数")
