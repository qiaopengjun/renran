from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'
    verbose_name = '文章管理'
    verbose_name_plural = verbose_name
