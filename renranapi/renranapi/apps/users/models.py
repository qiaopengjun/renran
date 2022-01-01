from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

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
