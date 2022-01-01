from django.contrib import admin
from .models import ArticleCollection, Article, ArticleSpecial


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


class ArticleSpecialModelAdmin(admin.ModelAdmin):
    """专题"""
    list_display = ["id", "name", "image_html", "notice", "article_count", "follow_count", "user"]
    ordering = ["id"]


admin.site.register(ArticleSpecial, ArticleSpecialModelAdmin)
