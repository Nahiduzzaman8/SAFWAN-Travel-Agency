from rest_framework import serializers
from .models import TourPackage
from datetime import date

class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_duration_days(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be at least 1 day.")
        return value

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("End date must be after start date.")
        if data["start_date"] < date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")
        return data
