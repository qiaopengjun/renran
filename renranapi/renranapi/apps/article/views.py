from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ArticleCollection, Article, ArticleImage, ArticleSpecial, ArticlePostSpecial
from .serializers import CollectionModelSerializer, ArticleModelSerializer, ArticleImageModelSerializer, \
    SpecialModelSerializer, ArticleRetrieveModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone as datetime
from rest_framework import status
from users.models import User
from renranapi.utils.tablestore import OTS
from renranapi.settings import constants
from renranapi.utils.tablestore import *
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action


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
        return Article.objects.filter(is_deleted=False, is_show=True, user=self.request.user,
                                      collection_id=collection_id).order_by("orders", "id")

    def patch(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)
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
            # 取消推送Feed流
            article.cancel_push_feed()
            # self.cancel_push_feed(article)
        else:
            """发布文章"""
            article.is_public = True
            # 推送feed流给粉丝
            article.push_feed()
            # self.push_feed(article)
        article.save()
        return Response({"detail": "发布状态切换成功!"})

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        collection_id = int(request.data.get("collection"))
        article.collection_id = collection_id
        article.save()
        return Response({"detail": "移动文章成功!"})

    # @staticmethod
    # def push_feed(article):
    #     """推送feed流"""
    #     # 获取当前作者的粉丝列表
    #     flowers_list = ArticleAPIView.get_author_flowers(article.user.id)
    #     if len(flowers_list) < 1:
    #         return False
    #
    #     # 把推送数据填写到同步库中
    #     primary_key_list = [{
    #         "id": constants.MESSAGE_TABLE_ID,
    #         "user_id": flower,  # 粉丝ID
    #         "sequence_id": PK_AUTO_INCR,
    #         "message_id": article.id
    #     } for flower in flowers_list]
    #
    #     # 增加属性
    #     attribute_columns_list = [{
    #         "timestamp": datetime.now().timestamp(),  # 推送时间
    #         "is_read": False,  # 是否阅读
    #         "is_cancel": False,  # 是否取消推送
    #     } for flower in flowers_list]
    #
    #     ret = OTS().add_list("user_message_table", primary_key_list, attribute_columns_list)
    #     print(f"ret{ret}")
    #
    # @staticmethod
    # def get_author_flowers(author_id):
    #     """获取当前作者的所有粉丝"""
    #     start_key = {"id": 1, "user_id": author_id, "follow_user_id": INF_MIN}  # 查询开始的主键列
    #     end_key = {"id": 1, "user_id": author_id, "follow_user_id": INF_MAX}  # 查询结束的主键列
    #     data = []
    #     # 获取粉丝数据，默认一次最多只能获取90
    #     ret = OTS().get_list("user_relation_table", start_key, end_key)
    #     if ret["status"]:
    #         data.extend(ret["data"])
    #         while ret["token"]:  # 当数据超过90条时，token表示下一次查询的开始主键列
    #             start_key = ret["token"]
    #             ret = OTS().get_list("user_relation_table", start_key, end_key)
    #             data.extend(ret["data"])
    #
    #     flowers_list = [item["follow_user_id"] for item in data]
    #     print(f"flowers_list=={flowers_list}")
    #     return flowers_list
    #
    # @staticmethod
    # def cancel_push_feed(article):
    #     # 取消推送记录
    #     # 把推送数据填写到同步库中
    #     primary_key_list = ArticleAPIView.get_feed_list(article)  # 查询当前文章的所有推送记录
    #     print(primary_key_list)
    #     if len(primary_key_list) < 1:
    #         return False
    #
    #     attribute_columns_list = [{"is_cancel": True} for i in primary_key_list]
    #     OTS().update_list("user_message_table", primary_key_list, attribute_columns_list)
    #
    # @staticmethod
    # def get_feed_list(article):
    #     """获取指定文章的推送记录"""
    #     start_key = {
    #         "id": constants.MESSAGE_TABLE_ID,
    #         "user_id": INF_MIN,
    #         "sequence_id": INF_MIN,
    #         "message_id": article.id
    #     }
    #     end_key = {
    #         "id": constants.MESSAGE_TABLE_ID,
    #         "user_id": INF_MAX,
    #         "sequence_id": INF_MAX,
    #         "message_id": article.id
    #     }
    #     # 获取文章推送记录，默认一次最多只能获取90
    #     ret = OTS().get_list("user_message_table", start_key, end_key)
    #
    #     data = []
    #     if ret["status"]:
    #         data.extend(ret["data"])
    #         while ret["token"]:  # 当数据超过90条时，token表示下一次查询的开始主键列
    #             start_key = ret["token"]
    #             ret = OTS().get_list("user_message_table", start_key, end_key)
    #             data.extend(ret["data"])
    #
    #     return data


class ArticleInfoAPIView(APIView):
    """文章信息"""
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        if article.is_public:
            return Response({"detail": "已经发布的文章不能设置定时发布!"})

        # 判断定时发布的时候是否是未来时间
        now_time = datetime.now().timestamp()
        pub_time_str = request.data.get("pub_date")
        put_time = datetime.datetime.strptime(pub_time_str, "%Y-%m-%d %H:%M:%S").timestamp()
        if put_time <= now_time:
            return Response({"detail": "定时发布的文章必须是未来的时间点!"}, status=status.HTTP_400_BAD_REQUEST)

        article.pub_date = pub_time_str
        article.save()

        return Response({"detail": "定时发布文章设置成功!"})

    def put(self, request, pk):
        """文章内容保存"""
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        article.title = request.data.get("title")
        article.content = request.data.get("content")
        article.html_content = request.data.get("html_content")
        article.save()

        return Response({"detail": "编辑文章保存成功!"})


class ArticleImageAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageModelSerializer


class SpecialAPIView(ListAPIView):
    """专题视图"""
    permission_classes = [IsAuthenticated]
    serializer_class = SpecialModelSerializer

    def get_queryset(self):
        # /article/special/
        article_id = self.request.query_params.get("article_id")
        print(f"article_id {article_id}")
        # 使用逆向字段作为条件查询数据
        special_list = ArticleSpecial.objects.filter(is_deleted=False, is_show=True,
                                                     mymanager__user=self.request.user).order_by("orders", "id")
        for special in special_list:
            # 给每一个专题模型新增一个字段，表示当前文章的收录状态
            special.post_status = special.check_post_status(article_id)

        return special_list


class ArticlePostAPIView(APIView):
    """文章投稿"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """文章投稿到专题"""
        # 文章ID和专题ID
        article_id = request.data.get("article_id")
        special_id = request.data.get("special_id")
        try:
            article = Article.objects.get(pk=article_id, is_deleted=False, is_show=True, user=self.request.user)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            special = ArticleSpecial.objects.get(pk=special_id, is_deleted=False, is_show=True)
        except ArticleSpecial.DoesNotExist:
            return Response({"detail": "当前专题不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        # 判断当前文章是否已经投稿并在审核中或者已经收录了
        try:
            ArticlePostSpecial.objects.get(article=article, special=special, status__in=[0, 1, 2])
            return Response({"detail": "当前文章已经在投稿中或已被收录，请不要频繁点击投稿!"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        # 新增投稿记录
        postlog = ArticlePostSpecial.objects.create(
            article=article,
            special=special,
            status=0,
            post_time=datetime.now()
        )

        # 判断当前用户是否是专题管理员，如果是，则直接默认审核通过
        try:
            # 当前投稿文章作者是专题管理员
            postlog.special.mymanager.get(user=request.user)
            postlog.status = 2  # 默认审核通过
            postlog.save()
        except:
            pass

        # 返回响应信息
        return Response({"detail": "投稿成功！"})


class ArticleRetrieveAPIView(RetrieveAPIView):
    """文章详情"""
    queryset = Article.objects.filter(is_deleted=False, is_show=True, is_public=True)
    serializer_class = ArticleRetrieveModelSerializer


class FocusAPIView(APIView):
    """在文章详情页中判断当前用户是否关注了文章作者"""

    def get(self, request):
        if not isinstance(request.user, User):
            return Response({"status": -2, "detail": "当前用户尚未登录！无法查询关注关系"})

        try:
            author_id = int(request.query_params.get("author_id"))
            User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"detail": "参数有误，当前作者不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        if author_id == request.user.id:
            return Response({"status": -1, "detail": "当前用户是作者!"})

        ret = OTS().get_row("user_relation_table", {"id": constants.RELATION_TABLE_ID, "user_id": author_id,
                                                    "follow_user_id": request.user.id})
        return Response({"status": int(ret[0])})

    def put(self, request):
        """切换关注关系"""
        if not isinstance(request.user, User):
            return Response({"detail": "用户尚未登录，无法操作"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            author_id = int(request.data.get("author_id"))
            User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"detail": "参数有误，当前作者不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        if author_id == request.user.id:
            return Response({"detail": "当前用户是作者!"}, status=status.HTTP_400_BAD_REQUEST)

        focus_status = bool(int(request.data.get("status")))

        client = OTS()
        primary_key = {"id": constants.RELATION_TABLE_ID, "user_id": author_id, "follow_user_id": request.user.id}
        if focus_status:
            message = "取消关注"
            ret = client.delete_row("user_relation_table", primary_key)
        else:
            message = "关注"
            ret = client.put_row("user_relation_table", primary_key)

        if ret[0] is False:
            return Response({"detail": "%s失败！" % message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"detail": "%s成功！" % message})


class UserArticleAPIView(ViewSet):
    permission_classes = [IsAuthenticated]
    """用户和文章之间的交互行为记录api"""
    client = OTS()

    def check_params(self):
        user = self.request.user
        pk = int(self.kwargs.get("pk"))
        try:
            article = Article.objects.get(pk=pk, is_deleted=False, is_show=True, is_public=True)
        except Article.DoesNotExist:
            return Response({"detail": "当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        # 如果用户是作者，则不需要记录
        if article.user.id == user.id:
            return Response({"detail": "当前用户是作者！"}, status=status.HTTP_400_BAD_REQUEST)

        primary_key = {"id": constants.LOG_TABLE_ID, "user_id": user.id, "message_id": pk}
        ret = self.client.get_row("user_message_log_table", primary_key)

        return user, primary_key, ret

    @action(methods=["get"], detail=True)
    def read(self, request, pk):
        response = self.check_params()
        if isinstance(response, Response):
            return response
        user, primary_key, ret = response
        if ret[0] and len(ret[1]) < 1:
            attribute_columns = {
                "is_read": 1,
                "is_comment": 0,
                "is_reward": 0,
                "is_like": 0,
                "timestamp": datetime.now().timestamp(),
            }
            self.client.put_row("user_message_log_table", primary_key, attribute_columns)

        return Response({"detail": "ok"})

    @action(methods=["get"], detail=True)
    def status(self, request, pk):
        """添加评论，点赞等行为"""
        # todo 收藏
        response = self.check_params()
        if isinstance(response, Response):
            return response
        user, primary_key, ret = response
        status_type = request.query_params.get("type")
        if status_type not in ("is_comment", "is_like"):
            return Response({"detail": "参数有误，无法添加行为记录"}, status=status.HTTP_400_BAD_REQUEST)
        if ret[0] and len(ret[1]) > 0:
            attribute_columns = {
                status_type: 1,
                "timestamp": datetime.now().timestamp(),
            }
            self.client.update_row("user_message_log_table", primary_key, attribute_columns)
        else:
            return Response({"detail": "当前用户没有阅读文章的记录，无法添加行为记录"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "ok"})
