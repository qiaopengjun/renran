from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # 密码加密功能
from django.utils.translation import gettext, gettext_lazy as _
from .models import User


# Register your models here.
class UserModelAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ["id", "avatar_small", "username",  "mobile"]
    # # fieldsets 和 add_fieldsets 都在从UserAdmin中复制粘贴过来，重写加上自己需要的字段的。
    # 更新数据时的表单配置项
    fieldsets = (
        (None, {'fields': ('username', 'password', "avatar")}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # 添加数据时的表单配置项
    add_fieldsets = (
        ("必填项", {
            'classes': ('wide',),
            'fields': ('username', "mobile", 'password1', 'password2', "avatar"),
        }),
        ('可选项', {
            'classes': ('collapse',),  # 折叠样式
            'fields': (),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    ordering = ("id",)
    # 分页配置，一页数据量
    list_per_page = 10


admin.site.register(User, UserModelAdmin)
