from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from renranapi.settings import constants
from django.utils import timezone as datetime


"""
注意：开发中绝对不能把当前时间now写在视图方法外面或者作为类属性的值,
因为外面的代码或类属性的值会在项目初始化的时候就执行了而且只执行一遍，
这样的话，项目运行时，now的值就不会发生变化，自然也就不是代表当前时间了，而是代表了项目运行的初始化时间，所以会出bug。
"""


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
        """重写"""
        return Banner.objects.filter(
            is_deleted=False,
            is_show=True,
            start_time__lte=datetime.now(),
            end_time__gte=datetime.now()
        ).order_by("orders", "id")[:constants.HOME_BANNER_LENGTH]
