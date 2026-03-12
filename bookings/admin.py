from django.contrib import admin
from .models import TourBooking


@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "tour_package",
        "number_of_people",
        "status",
        "booking_date",
    )

    search_fields = ("user__username", "tour_package__title")
    list_filter = ("status", "booking_date")