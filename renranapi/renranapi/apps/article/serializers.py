from rest_framework import serializers
from .models import ArticleCollection


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
