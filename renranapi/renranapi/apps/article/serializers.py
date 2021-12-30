from rest_framework import serializers
from .models import ArticleCollection, Article
from django.utils import timezone as datetime


class CollectionModelSerializer(serializers.ModelSerializer):
    """文集序列化器"""

    class Meta:
        model = ArticleCollection
        fields = ["id", "name"]

    def validate(self, attrs):
        # 必须保证同一个用户的文集名称是唯一的
        name = attrs.get("name")
        # 获取当前登录用户信息，可以直接通过self.context["request"]
        user = self.context["request"].user
        try:
            ArticleCollection.objects.get(user=user, name=name, is_deleted=False)
            raise serializers.ValidationError("对不起，当前文集已存在！")
        except ArticleCollection.DoesNotExist:
            return attrs

    def create(self, validated_data):
        name = validated_data.get("name")
        user = self.context["request"].user
        try:
            instance = ArticleCollection.objects.create(
                name=name,
                user=user
            )
            return instance
        except:
            raise serializers.ValidationError("添加文集失败！")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()
        return instance


class ArticleModelSerializer(serializers.ModelSerializer):
    """文章序列化器"""
    insert = serializers.BooleanField(write_only=True, required=False, default=True,
                                      help_text="新增文章的排序位置: True表示开头,False表示末尾")

    class Meta:
        model = Article
        fields = ["id", "title", "content", "html_content", "is_public", "pub_date", "insert"]

    def create(self, validated_data):
        """添加文章"""
        # 如果希望在序列化器中获取视图中的路由参数,必须先获取视图对象
        # self.context["view"] # 调用当前序列化器的视图对象
        # self.context["request"] # 本次客户端发送的http请求
        # self.context["format"]  # 本次客户端期望服务端发送的数据格式
        collection_id = int(self.context["view"].kwargs.get("collection"))

        instance = Article.objects.create(
            title=datetime.now().strftime("%Y-%m-%d"),
            user=self.context["request"].user,
            collection_id=collection_id,
        )

        # 处理文章的顺序
        if not validated_data.get("insert"):
            """把文章调整到末尾"""
            instance.orders = 0 - instance.id
            instance.save()

        return instance
