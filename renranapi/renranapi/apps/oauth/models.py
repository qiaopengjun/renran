from django.db import models
from renranapi.utils.models import BaseModel
from users.models import User


# Create your models here.
class OauthUser(BaseModel):
    """第三方登录用户信息"""
    NAME_TYPE = (
        (1, "QQ"),
        (2, "微信"),
        (3, "微博"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="open_user", verbose_name='用户')
    openid = models.CharField(max_length=64, unique=True, verbose_name='openid')
    name = models.IntegerField(choices=NAME_TYPE, default=1, verbose_name="社交平台名称")
    access_token = models.CharField(max_length=500, verbose_name="临时访问票据", help_text="有效期:3个月")
    refresh_token = models.CharField(max_length=500, verbose_name="刷新访问票据的token",
                                     help_text="当access_token过期以后,可以使用refresh_token来重新获取新的access_token和refresh_token")

    class Meta:
        db_table = 'rr_oauth_user'
        verbose_name = '第三方社交账号登录用户数据'
        verbose_name_plural = verbose_name
