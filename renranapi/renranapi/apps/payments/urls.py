from django.urls import path
from . import views

urlpatterns = [
    path("alipay/", views.AlipayAPIView.as_view()),
]
