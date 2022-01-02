import random
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone as datetime
from django.conf import settings
from article.models import Article
from alipay import AliPay
from .models import Reward


# Create your views here.
class AlipayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """发起支付，生成记录，返回支付链接"""
        # 创建打赏记录
        money = request.data.get("money")
        article_id = request.data.get("article_id")
        user = request.user
        try:
            article = Article.objects.get(is_deleted=False, is_show=True, is_public=True, pk=article_id)
        except:
            return Response({"detail": "打赏的文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 生成订单号
        trade_no = datetime.now().strftime("%Y%m%d%H%M%S") + ("%06d" % user.id) + ("%06d" % random.randint(1, 999999))

        reward = Reward.objects.create(
            user=user,
            money=float(money),
            article=article,
            reward_type=1,
            message=request.data.get("message"),
            trade_no=trade_no,
        )

        # 读取秘钥文件的内容
        app_private_key_string = open(settings.ALIPAY.get("app_private_key_path")).read()
        alipay_public_key_string = open(settings.ALIPAY.get("alipay_public_key_path")).read()
        # 根据支付宝sdk生成支付链接
        alipay = AliPay(
            appid=settings.ALIPAY.get("appid"),  # appid
            app_notify_url=settings.ALIPAY.get("app_notify_url"),  # 默认回调url
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type=settings.ALIPAY.get("sign_type"),
            debug=settings.ALIPAY.get("debug")
        )

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=trade_no,  # 订单号
            total_amount=float(money),  # 订单金额
            subject="打赏文章《%s》" % article.title,  # 订单标题
            return_url=settings.ALIPAY.get("return_url"),  # 订单的同步回调地址[js跳转]
            notify_url=settings.ALIPAY.get("notify_url")  # 订单的异步回调地址[由支付宝主动发起请求到api服务端的地址]
        )

        url = settings.ALIPAY.get("gateway_url") + order_string

        return Response(url)
