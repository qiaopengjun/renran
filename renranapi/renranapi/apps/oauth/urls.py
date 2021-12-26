from django.urls import path, re_path
from . import views

urlpatterns = [
    path("qq/", views.QQUserLoginViewSet.as_view({"get": "url"})),
    path("qq/user/", views.QQUserLoginViewSet.as_view({"get": "get_qq_user"})),
]
