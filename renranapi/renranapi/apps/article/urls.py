from django.urls import path, re_path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("collection/", views.CollectionAPIView.as_view()),
    re_path(r"^collection/(?P<pk>\d+)/$", views.CollectionAPIView.as_view()),
    re_path(r"^collection/(?P<collection>\d+)/articles/$", views.ArticleAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/$", views.ArticleAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/interval/$", views.ArticleInfoAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/info/$", views.ArticleInfoAPIView.as_view()),
    path("image/", views.ArticleImageAPIView.as_view()),
    path("special/", views.SpecialAPIView.as_view()),
    path("post/", views.ArticlePostAPIView.as_view()),
    re_path(r"^(?P<pk>\d+)/retrieve/$", views.ArticleRetrieveAPIView.as_view()),
    path("focus/", views.FocusAPIView.as_view()),
]

router = SimpleRouter()
router.register("log", views.UserArticleAPIView, basename="log")
urlpatterns += router.urls
