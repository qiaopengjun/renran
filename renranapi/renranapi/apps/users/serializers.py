import re
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from .models import User
from django_redis import get_redis_connection

class UserModelSerializer(serializers.ModelSerializer):
    """用户信息的序列化器"""
    # 验证字段
    sms_code = serializers.CharField(max_length=6, min_length=4, required=True, write_only=True, help_text="短信验证码",
                                     label="短信验证码")
    token = serializers.CharField(max_length=1000, read_only=True, label="jwt登录令牌")

    # 模型信息
    class Meta:
        model = User
        fields = ["id", "username", "mobile", "password", "nickname", "sms_code", "token"]
        extra_kwargs = {
            "nickname": {"required": True, },
            "password": {"write_only": True, "min_length": 6, "max_length": 16, },
            "mobile": {"write_only": True},
            "username": {"read_only": True},
        }

    # 验证数据方法
    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r"^1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError("手机号码格式不正确！")

        # 验证短信验证码
        client_sms_code = attrs.get("sms_code")
        redis_conn = get_redis_connection("sms_code")
        server_sms_code_bytes = redis_conn.get("sms_%s" % mobile)
        if server_sms_code_bytes is None:
            raise serializers.ValidationError("短信验证码已过期!")

        server_sms_code = server_sms_code_bytes.decode()
        if server_sms_code != client_sms_code:
            raise serializers.ValidationError("短信验证码错误!请重新确认!")
        else:
            # 验证通过以后,redis中的验证码就没有必要保留了
            redis_conn.delete("sms_%s" % mobile)

        # 验证码校验通过以后，不需要保存验证码到数据库中, 所以删除验证码
        attrs.pop("sms_code")
        return attrs

    # 模型更新和添加操作
    def create(self, validated_data):
        """用户注册"""
        # 添加用户
        try:
            user = User.objects.create_user(
                username=validated_data.get("mobile"),  # 手机号作为用户名
                mobile=validated_data.get("mobile"),
                nickname=validated_data.get("nickname"),
            )
        except:
            raise serializers.ValidationError("用户注册失败！")

        # 密码要加密
        user.set_password(validated_data.get("password"))
        user.save()

        # 返回jwt登录状态

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user
