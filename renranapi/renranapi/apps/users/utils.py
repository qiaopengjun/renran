from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :param token: jwt token字符串
    :param user: 本次成功登录的用户模型对象
    :param request: 本次登录用户的http请求对象
    :return: dict
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username if user.username else "暂无",
        'avatar': user.avatar.url if user.avatar else "",
    }


def get_user_by_account(account):
    try:
        return User.objects.get(Q(username=account) | Q(mobile=account) | Q(email=account))
    except User.DoesNotExist:
        return None


class CustomAuthUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 根据客户端提交的账户信息获取用户模型对象
        user = get_user_by_account(username)
        # 账号通过了还要进行密码的验证,以及判断当前账户是否是激活状态 是否允许登录认证
        if user is not None and user.check_password(raw_password=password) and self.user_can_authenticate(user):
            return user
