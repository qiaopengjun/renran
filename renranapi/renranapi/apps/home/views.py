from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner, Nav
from .serializers import BannerModelSerializer, NavModelSerializer, ArticleModelSerializer
from renranapi.settings import constants
from django.utils import timezone as datetime
from article.models import Article
from .paginations import HomeArticlePageNumberPagination
from .serializers import ArticleModelSerializer
from users.models import User
from renranapi.utils.tablestore import *

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


class HeaderNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, pid=None, is_deleted=False, position=1).order_by("orders", "id")[
               :constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, pid=None, is_deleted=False, position=2).order_by("orders", "id")[
               :constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleModelSerializer
    pagination_class = HomeArticlePageNumberPagination
    # queryset = Article.objects.filter(is_public=True, is_show=True, is_deleted=False).order_by("-reward_count", "-comment_count", "-like_count", "-id")

    def get_queryset(self):
        user = self.request.user

        if isinstance(self.request.user, User):
            """登录"""
            start_key = {"id": constants.MESSAGE_TABLE_ID, "user_id": user.id, "sequence_id": INF_MIN,
                         "message_id": INF_MIN}
            end_key = {"id": constants.MESSAGE_TABLE_ID, "user_id": user.id, "sequence_id": INF_MAX,
                       "message_id": INF_MAX}
            cond = SingleColumnCondition("is_cancel", False, ComparatorType.EQUAL)
            message_list = []
            # 接受客户端执行返回的单页数据量，如果客户端没有指定，则默认采用分页器的单页数据量
            size = int(self.request.query_params.get("size")) or self.pagination_class.page_size
            ret = OTS().get_list("user_message_table", start_key, end_key, limit=size, cond=cond)
            if ret:
                for item in ret["data"]:
                    message_list.append(item["message_id"])
                while ret["token"]:
                    # print(ret["token"]) # [('id', 1), ('user_id', 2), ('sequence_id', 1596081490522997), ('message_id', 23)]
                    start_key = ret["token"]
                    end_key = {"id": constants.MESSAGE_TABLE_ID, "user_id": user.id, "sequence_id": INF_MAX,
                               "message_id": INF_MAX}
                    cond = SingleColumnCondition("is_cancel", False, ComparatorType.EQUAL)
                    ret = OTS().get_list("user_message_table", start_key, end_key, limit=size, cond=cond)
                    for item in ret["data"]:
                        message_list.append(item["message_id"])

            print(f"message_list{message_list}")
            queryset = Article.objects.filter(is_public=True, is_show=True, is_deleted=False,
                                              pk__in=message_list).order_by("-id")
            print(f"queryset{queryset}")
        else:
            queryset = Article.objects.filter(is_public=True, is_show=True, is_deleted=False).order_by("-reward_count",
                                                                                                       "-comment_count",
                                                                                                       "-like_count",
                                                                                                       "-id")
        print(f"queryset1 {queryset}")
        return queryset
