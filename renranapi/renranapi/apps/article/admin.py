from django.contrib import admin
from .models import ArticleCollection


# Register your models here.
class ArticleCollectionModelAdmin(admin.ModelAdmin):
    """文集"""
    list_display = ["id", "name"]
    ordering = ["id"]


admin.site.register(ArticleCollection, ArticleCollectionModelAdmin)
