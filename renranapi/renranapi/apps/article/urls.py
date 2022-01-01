from django.urls import path, re_path
from . import views

urlpatterns = [
    path("collection/", views.CollectionAPIView.as_view()),
    re_path(r"^collection/(?P<pk>\d+)/$", views.CollectionAPIView.as_view()),
    re_path(r"^collection/(?P<collection>\d+)/articles/$", views.ArticleAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/$", views.ArticleAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/interval/$", views.ArticleInfoAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/info/$", views.ArticleInfoAPIView.as_view()),
]
