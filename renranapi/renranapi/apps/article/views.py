from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ArticleCollection
from .serializers import CollectionModelSerializer


# Create your views here.
class CollectionAPIView(ListAPIView):
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
            collection_list = [
                {
                    "id": collection1.id,
                    "name": collection1.name
                },
                {
                    "id": collection2.id,
                    "name": collection2.name
                }
            ]
        return collection_list
