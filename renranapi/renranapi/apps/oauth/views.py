from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from users.serializers import UserModelSerializer
from .utils import OAuthQQ, QQNetworkError
from .models import OauthUser
from users.utils import CustomAuthUserModelBackend


# Create your views here.
class QQUserLoginViewSet(ViewSet):
    def url(self, request):
        """获取QQ登录地址"""
        qq = OAuthQQ(**settings.QQ_CONNECT)
        url = qq.url()
        return Response(url)

    def get_qq_user(self, request):
        """获取登录用户信息"""
        # 1. 获取客户端提交过来的code授权码
        code = request.query_params.get("code")
        state = request.query_params.get("state")
        if code is None:
            return Response({"detail": "对不起,QQ登录授权码丢失,请重新使用QQ登录!"})

        qq = OAuthQQ(**settings.QQ_CONNECT)
        try:
            # 2. 根据授权码获取access_token临时访问票据
            access_token, refresh_token = qq.get_access_token(code)
            # 3. 根据临时访问票据获取QQ用户的openID
            openid = qq.get_open_id(access_token)
            print(f"openid=={openid}")  # openid==5AA16A7311CBB11295F01FB2A3D8F413
        except QQNetworkError:
            return Response({"detail": "网络发生异常,QQ登录失败!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 4. 根据openid到数据库是否有QQ用户信息绑定记录
        try:
            qq_user = OauthUser.objects.get(name=1, openid=openid)
            print(f"qq_user.user.username=={qq_user.user.username}")
            """表示当前用户已经和QQ进行登录绑定,生成jwt状态即可"""
            # 返回jwt登录状态
            from rest_framework_jwt.settings import api_settings

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(qq_user.user)
            qq_user.user.token = jwt_encode_handler(payload)
            serializer = UserModelSerializer(instance=qq_user.user)
            return Response(serializer.data)

        except OauthUser.DoesNotExist:
            """表示当前用户没有进行QQ登录绑定,则让客户端显示绑定QQ和用户信息的表单页面"""

        # 5. 根据数据库查询结果返回登录状态或者进行QQ与用户信息绑定流程
        return Response({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "openid": openid,
        })

    def qq_user_login(self, request):
        """网站用户和QQ进行绑定"""
        # 接收客户端提交
        username = request.data.get("username")
        password = request.data.get("password")
        # 单点调试
        # 查询用户是否存在
        model_backend = CustomAuthUserModelBackend()
        user = model_backend.authenticate(request, username, password)
        if user is None:
            return Response({"detail": "用户信息不存在或密码错误!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            """绑定账号和QQ"""
            return self._qq_user_bind(request, user)

    def _qq_user_bind(self, request, user):
        """平台账号绑定QQ信息"""
        access_token = request.data.get("access_token")
        openid = request.data.get("openid")
        refresh_token = request.data.get("refresh_token")
        try:
            OauthUser.objects.create(
                user=user,
                openid=openid,
                name=1,
                access_token=access_token,
                refresh_token=refresh_token,
            )

            # 返回jwt登录状态
            from rest_framework_jwt.settings import api_settings

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            user.token = jwt_encode_handler(payload)
            serializer = UserModelSerializer(instance=user)
            return Response(serializer.data)
        except:
            return Response({"detail": "绑定QQ账号失败!请联系客服工作人员!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
