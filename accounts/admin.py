from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Fields to display in admin list
    list_display = ("id", "username", "email", "phone", "role", "is_staff", "is_superuser")
    # Fields editable in admin form
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "phone", "role")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "phone", "role", "is_staff", "is_superuser")
        }),
    )
    search_fields = ("username", "email", "phone")
    ordering = ("id",)

admin.site.register(User, UserAdmin)
