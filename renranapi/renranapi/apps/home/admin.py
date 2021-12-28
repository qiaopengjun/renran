from django.contrib import admin
from .models import Banner, Nav
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
# 设置网页title
admin.site.site_title = "荏苒资讯"
# 设置站点header
admin.site.site_header = "荏苒资讯"


class NavModelAdmin(admin.ModelAdmin):
    """导航菜单的模型管理器"""
    list_display = ["id", "name", "link", "is_http", "position"]
    ordering = ["id"]


admin.site.register(Nav, NavModelAdmin)


class BannerModelAdmin(admin.ModelAdmin):
    """轮播广告的模型管理器"""
    list_display = ["id", "name", "link", "is_show", "image_html", "start_time", "end_time"]
    list_editable = ["is_show", "start_time", "end_time"]
    ordering = ["id"]
    search_fields = ("name",)
    list_per_page = 10


admin.site.register(Banner, BannerModelAdmin)
