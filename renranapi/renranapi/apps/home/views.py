from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from renranapi.settings import constants
from django.utils import timezone as datetime


# Create your views here.
class BannerListAPIView(ListAPIView):
    """轮播图列表"""
    # bug: datetime.now()的值不是我们想当然的当前时间戳,而是项目启动时间
    # queryset = Banner.objects.filter(
    #     is_deleted=False,
    #     is_show=True,
    #     start_time__lte=datetime.now() # 这里的一个bug,代表了代码运行的那个当时时间戳.
    # ).order_by("orders","id")[:constants.HOME_BANNER_LENGTH]
    serializer_class = BannerModelSerializer

    def get_queryset(self):
        """"""
        return Banner.objects.filter(
            is_deleted=False,
            is_show=True,
            start_time__lte=datetime.now(),
            end_time__gte=datetime.now()
        ).order_by("orders", "id")[:constants.HOME_BANNER_LENGTH]
