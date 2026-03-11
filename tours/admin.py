from django.contrib import admin
from .models import TourPackage

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "destination", "price", "duration_days", "available_seats", "start_date", "end_date")
    search_fields = ("title", "destination")
    list_filter = ("start_date", "end_date")
