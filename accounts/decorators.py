from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .utils import decode_jwt

def jwt_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return Response({"error": "Authorization header missing"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token_type, token = auth_header.split(" ")
        except ValueError:
            return Response({"error": "Invalid Authorization header"}, status=status.HTTP_401_UNAUTHORIZED)

        if token_type != "Bearer":
            return Response({"error": "Authorization must start with Bearer"}, status=status.HTTP_401_UNAUTHORIZED)

        payload = decode_jwt(token)
        if not payload:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            request.user = User.objects.get(id=payload["user_id"])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

        return func(self, request, *args, **kwargs)
    return wrapper
