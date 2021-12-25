from django.urls import path, re_path
from . import views

urlpatterns = [
    path("qq/", views.QQUserLoginViewSet.as_view({"get": "url"}))
]
