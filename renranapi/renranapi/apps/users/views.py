import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from urllib.parse import urlencode  # urllib python内置的标准模块，用于发送http请求，类似vue里面的axios
from urllib.request import urlopen
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer


# Create your views here.
class CaptchaAPIView(APIView):
    """验证码"""

    def get(self, request):
        """接受客户端提交的验证码相关信息"""
        params = {
            "aid": settings.TENCENT_CAPTCHA.get("APPID"),
            "AppSecretKey": settings.TENCENT_CAPTCHA.get("App_Secret_Key"),
            "Ticket": request.query_params.get("ticket"),
            "Randstr": request.query_params.get("randstr"),
            # request._request表示获取django框架的request对象
            # request._request.META获取本次客户端的请求头
            "UserIP": request._request.META.get("REMOTE_ADDR")
        }
        # 把字典数据转换成地址栏的查询字符串格式
        # aid=xxx&AppSecretKey=xxx&xxxxx
        params = urlencode(params)
        url = settings.TENCENT_CAPTCHA.get("GATEWAY")
        # 发送http的get请求
        # urlopen(url=请求地址，data=请求体数据)
        # 如果get请求，只需要填写参数1
        # 如果post请求，则需要填写参数1和参数2，其中参数2的格式为字典格式
        # urlopen是一个资源对象
        f = urlopen("%s?%s" % (url, params))
        # https://ssl.captcha.qq.com/ticket/verify?aid=xxx&AppSecretKey=xxx&xxxxx

        # f.read() 读取响应信息
        content = f.read()
        # json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
        res = json.loads(content)
        if int(res.get("response")) == 1:
            # 验证成功
            return Response({"detail": 1})
        else:
            # 验证失败
            return Response({"detail": 0}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(CreateAPIView):
    """用户信息"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
