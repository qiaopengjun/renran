from django.urls import path, re_path
from . import views

urlpatterns = [
    path("table/", views.TableAPIView.as_view()),
]
