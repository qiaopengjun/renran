import json, random
import logging
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
from django_redis import get_redis_connection
from ronglian_sms_sdk import SmsSDK
from django.conf import settings
from renranapi.settings import constants
# 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决
from mycelery.sms.tasks import send_sms

logger = logging.getLogger("django")


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


class SMSAPIView(APIView):
    """
    短信api接口
    /users/sms/(?P<mobile>1[3-9]\d{9})/
    """

    def get(self, request, mobile):
        """发送短信"""
        redis_conn = get_redis_connection("sms_code")
        # 1. 限制用户60s内只能发送一条短信[基于redis中的字符串有效期来完成]
        ret = redis_conn.get("interval_%s" % mobile)
        if ret is not None:
            # 如果ret有值,则表示60s内用户曾经发送短信,不能让用户频繁发送
            return Response({"detail": "对不起, 发送短信过于频繁!"})

        # 2. 生成6位随机验证码
        sms_code = "%06d" % (random.randint(1, 999999))

        # 3. 保存验证码和手机到redis中
        # 3.1 初始化管道对象
        pipe = redis_conn.pipeline()
        # 3.2 开启事务
        pipe.multi()
        # 3.3 添加本次事务相关的命令到管道对象中,注意,管道中的命令不会被自动执行
        pipe.setex("sms_%s" % mobile, constants.SMS_EXPIRE_TIME, sms_code)
        pipe.setex("interval_%s" % mobile, constants.SMS_INTERVAL_TIME, "_")
        # 3.4 执行管道中所有命令,也就是事务提交
        pipe.execute()  # 上面所有的命令都被一次性执行,要么一起成功,要么一起失败!

        # 发送短信
        # 实例化短信接口SDK对象
        # sdk = SmsSDK(settings.SMS["accId"], settings.SMS["accToken"], settings.SMS["appId"])
        # # 短信模板中的数据: 测试模板格式: 云通讯】您的验证码是{1}，请于{2}分钟内正确输入。
        # datas = (sms_code, constants.SMS_EXPIRE_TIME // 60)
        # resp = sdk.sendMessage(settings.SMS["tid"], mobile, datas)
        # resp = json.loads(resp)
        # if resp.get("statusCode") != "000000":
        #     # 记录错误信息
        #     logger.error("发送短信失败!手机号:%s" % mobile)

        # 2. 调用任务函数，发布任务
        send_sms.delay(mobile=mobile, sms_code=sms_code)
        # send_sms.delay() 如果调用的任务函数没有参数，则不需要填写任何内容

        # 返回响应信息
        return Response({"detail": "短信已发送!请留意您的手机短信!"})


class MobileAPIView(APIView):
    def get(self, request, mobile):
        try:
            User.objects.get(mobile=mobile)
            return Response({"detail": "当前手机号码已经被注册"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "ok"})
