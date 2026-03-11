from rest_framework import serializers
from .models import ContactMessage
import re

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate_phone(self, value):
        if value:
            if not re.fullmatch(r'^\+?\d{10,15}$', value):
                raise serializers.ValidationError("Phone number must be 10-15 digits, may include +.")
        return value

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value
