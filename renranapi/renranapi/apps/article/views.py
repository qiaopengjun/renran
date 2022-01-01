from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ArticleCollection, Article
from .serializers import CollectionModelSerializer, ArticleModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone as datetime


# Create your views here.
class CollectionAPIView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):
    """文集接口"""
    # 限制只能是登录用户才能访问操作当前视图的接口
    permission_classes = [IsAuthenticated]
    # queryset = ArticleCollection.objects.all()
    serializer_class = CollectionModelSerializer

    def get_queryset(self):
        # request.user # 代表的就是当前访问视图的用户[当然是用户已经登录的情况下]
        # self.request.user # 获取当前登录用户
        # print(self.request)
        # print(self.request.user)
        # return ArticleCollection.objects.filter(user__id=self.request.user.id)
        collection_list = ArticleCollection.objects.filter(is_deleted=False, is_show=True,
                                                           user=self.request.user).order_by("orders", "id")
        if len(collection_list) < 1:
            """针对新用户默认创建2个文集提供给用户[当然也可以在用户注册的时候给用户默认添加2个文集]"""
            collection1 = ArticleCollection.objects.create(name="日记本", user=self.request.user)
            collection2 = ArticleCollection.objects.create(name="随笔", user=self.request.user)
            collection_list = [collection1, collection2]
            # collection_list = [
            #     {
            #         "id": collection1.id,
            #         "name": collection1.name
            #     },
            #     {
            #         "id": collection2.id,
            #         "name": collection2.name
            #     }
            # ]
        return collection_list

    def perform_destroy(self, instance):
        # 逻辑删除文集
        instance.is_deleted = True
        instance.save()


class ArticleAPIView(ListAPIView, CreateAPIView):
    """文章视图接口"""
    # queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # /article/collection/<collection>\d/articles/
        # 获取路由参数的另一种方式 self.kwargs.get("参数名称")
        collection_id = self.kwargs.get("collection")
        print(collection_id)
        return Article.objects.filter(is_deleted=False, is_show=True, user=self.request.user,
                                      collection_id=collection_id).order_by("orders", "id")

    def patch(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"})

        """
              1. 隐私文章 is_public=False, pub_date=None
              2. 发布文章 is_public=True, pub_date=None
              3. 定时文章 is_public=False, pub_date=时间
              """
        if article.pub_date:
            """取消定时发布文章"""
            article.pub_date = None
        elif article.is_public:
            """把文章设置为隐私文章"""
            article.is_public = False
        else:
            """发布文章"""
            article.is_public = True

        # article.is_public = not article.is_public
        article.save()
        return Response({"detail": "发布状态切换成功!"})

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"})

        collection_id = int(request.data.get("collection"))
        article.collection_id = collection_id
        article.save()
        return Response({"detail": "移动文章成功!"})


class ArticleInfoAPIView(APIView):
    """文章信息"""
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"})

        if article.is_public:
            return Response({"detail": "已经发布的文章不能设置定时发布!"})

        # 判断定时发布的时候是否是未来时间
        now_time = datetime.now().timestamp()
        pub_time_str = request.data.get("pub_date")
        put_time = datetime.datetime.strptime(pub_time_str, "%Y-%m-%d %H:%M").timestamp()
        if put_time <= now_time:
            return Response({"detail": "定时发布的文章必须是未来的时间点!"})

        article.pub_date = pub_time_str
        article.save()

        return Response({"detail": "定时发布文章设置成功!"})

    def put(self, request, pk):
        """文章内容保存"""
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"})

        article.title = request.data.get("title")
        article.content = request.data.get("content")
        article.html_content = request.data.get("html_content")
        article.save()

        return Response({"detail": "编辑文章保存成功!"})
