from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .utils import OAuthQQ


# Create your views here.
class QQUserLoginViewSet(ViewSet):
    def url(self, request):
        """获取QQ登录地址"""
        qq = OAuthQQ(**settings.QQ_CONNECT)
        url = qq.url()
        return Response(url)
