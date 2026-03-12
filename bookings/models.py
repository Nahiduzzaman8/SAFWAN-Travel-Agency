from django.db import models
from django.conf import settings
from tours.models import TourPackage


class TourBooking(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    tour_package = models.ForeignKey(
        TourPackage,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    number_of_people = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.tour_package}"