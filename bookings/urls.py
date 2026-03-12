from django.urls import path
from .views import CreateBookingView, MyBookingsView, BookingDetailView

urlpatterns = [
    path("", CreateBookingView.as_view(), name="create-booking"),
    path("my/", MyBookingsView.as_view(), name="my-bookings"),
    path("<int:pk>/", BookingDetailView.as_view(), name="booking-detail"),
]