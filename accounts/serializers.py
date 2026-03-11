from rest_framework import serializers
from .models import User
import re

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "phone"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_phone(self, value):
        if value:
            if not re.fullmatch(r'^\+?\d{10,15}$', value):
                raise serializers.ValidationError("Phone number must be 10-15 digits, may include +.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data.get("phone", "")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
