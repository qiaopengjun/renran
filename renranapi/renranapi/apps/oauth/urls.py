from django.urls import path, re_path
from . import views

urlpatterns = [
    path("qq/", views.QQUserLoginViewSet.as_view({"get": "url"})),
    path("qq/user/", views.QQUserLoginViewSet.as_view({"get": "get_qq_user"})),
    path("qq/login/", views.QQUserLoginViewSet.as_view({"post": "qq_user_login"})),
    path("qq/reg/", views.QQUserLoginViewSet.as_view({"post": "qq_user_register"})),
]
