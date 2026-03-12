from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "message","email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
