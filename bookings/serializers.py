from rest_framework import serializers
from .models import TourBooking
from datetime import date


class TourBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourBooking
        fields = "__all__"
        read_only_fields = ("user", "status", "booking_date")

    def validate_number_of_people(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Number of people must be greater than zero."
            )
        return value

    def validate(self, data):

        tour = data["tour_package"]
        people = data["number_of_people"]

        # Rule 1: booking before start date
        if tour.start_date < date.today():
            raise serializers.ValidationError(
                "This tour has already started."
            )

        # Rule 2: available seats
        if people > tour.available_seats:
            raise serializers.ValidationError(
                "Not enough seats available."
            )

        return data

    def create(self, validated_data):

        tour = validated_data["tour_package"]
        people = validated_data["number_of_people"]

        # reduce seats
        tour.available_seats -= people
        tour.save()

        booking = TourBooking.objects.create(**validated_data)

        return booking

