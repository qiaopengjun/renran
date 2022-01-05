from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from renranapi.utils.tablestore import *
from renranapi.settings import constants
from django.utils import timezone as datetime

# Create your models here.
# AbstractUser 是django内部的auth模块里面声明的抽象模型，
# 抽象模型，是django内部用于提供给开发者声明模型父类的工具类，这种模型类，
# 在数据迁移的时候django不会为他们单独建表，所以这种模型的作用就是用于声明公共字段的
# 怎么声明一个django的抽象模型类？
"""
class 模型类(models.Model):
    字段列表
    字段列表
    class Meta:
        abstract = True # 表示当前模型是抽象模型
"""


class User(AbstractUser):
    nickname = models.CharField(max_length=20, null=True, verbose_name="用户昵称")
    mobile = models.CharField(max_length=15, unique=True, verbose_name="手机号")
    avatar = models.ImageField(upload_to="avatar", null=True, verbose_name="头像")
    wechat = models.CharField(max_length=100, null=True, unique=True, verbose_name="微信账号")
    alipay = models.CharField(max_length=100, null=True, unique=True, verbose_name="支付宝账号")
    qq_number = models.CharField(max_length=11, null=True, unique=True, verbose_name="QQ号")
    money = models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name="用户资金")

    class Meta:
        # 自定义表名
        db_table = "rr_users"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname if self.nickname else self.username

    def avatar_small(self):
        if self.avatar:
            return mark_safe(
                # f'<img style="border-radius: 0%;max-height: 60px; max-width: 200px;" src="{self.image.url}">')
                # f'<img style="border-radius: 100%;" src="{self.avatar.thumb_50x50.url}">')
                f'<img style="border-radius: 0%; max-height: 50px; max-width: 50px;" src="{self.avatar.url}">')
        return ""

    avatar_small.short_description = "个人头像(50x50)"
    avatar_small.allow_tags = True
    avatar_small.admin_order_field = "avatar"

    def get_user_log(self, user_id=None, limit=50):
        """获取指定用户最近3个月的行为记录"""
        if user_id is None:
            user_id = self.id
        start_key = {"id": constants.LOG_TABLE_ID, "user_id": user_id, "message_id": INF_MIN}
        end_key = {"id": constants.LOG_TABLE_ID, "user_id": user_id, "message_id": INF_MAX}
        columns_to_get = ["is_read", "is_comment", "is_reward", "is_like"]
        timestamp = datetime.now().timestamp() - 3 * 30 * 24 * 60 * 60
        cond = SingleColumnCondition("timestamp", timestamp, ComparatorType.GREATER_EQUAL)
        ret = OTS().get_list("user_message_log_table", start_key, end_key, limit=limit, columns_to_get=columns_to_get,
                             cond=cond)
        log_list = []
        if ret["status"]:
            """查询成功"""
            log_list.extend(ret["data"])
            while ret["token"] and len(log_list) < limit:
                ret = OTS().get_list("user_message_log_table", start_key, end_key, limit=limit,
                                     columns_to_get=columns_to_get, cond=cond)
                if ret["status"]:
                    log_list.extend(ret["data"])
        print(f"log_list{log_list}")
        return log_list

    def get_log_list(self, log_list):

        start_key = {"id": constants.LOG_TABLE_ID, "user_id": INF_MIN, "message_id": INF_MIN}
        end_key = {"id": constants.LOG_TABLE_ID, "user_id": INF_MAX, "message_id": INF_MAX}
        columns_to_get = ["is_read", "is_comment", "is_reward", "is_like"]
        timestamp = datetime.now().timestamp() - 15 * 24 * 60 * 60
        limit = 50
        user_list = set()
        for log_item in log_list:
            cond = CompositeColumnCondition(LogicalOperator.AND)
            cond.add_sub_condition(SingleColumnCondition("timestamp", timestamp, ComparatorType.GREATER_EQUAL))
            cond.add_sub_condition(SingleColumnCondition("message_id", log_item["message_id"], ComparatorType.EQUAL))
            ret = OTS().get_list("user_message_log_table", start_key, end_key, limit=limit,
                                 columns_to_get=columns_to_get, cond=cond)
            print(f"ret{ret}")
            if ret["status"]:
                for data in ret["data"]:
                    user_list.add(data["user_id"])
        print(f"user_list{user_list}")

        return list(user_list)
