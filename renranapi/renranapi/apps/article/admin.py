from django.contrib import admin
from .models import ArticleCollection, Article


# Register your models here.
class ArticleCollectionModelAdmin(admin.ModelAdmin):
    """文集"""
    list_display = ["id", "name"]
    ordering = ["id"]


admin.site.register(ArticleCollection, ArticleCollectionModelAdmin)


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "collection", "user", "is_public", "pub_date"]
    ordering = ["id"]


admin.site.register(Article, ArticleModelAdmin)
