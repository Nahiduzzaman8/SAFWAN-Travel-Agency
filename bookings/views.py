from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TourBooking
from .serializers import TourBookingSerializer
from accounts.decorators import jwt_required


class CreateBookingView(APIView):

    @jwt_required
    def post(self, request):

        serializer = TourBookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class MyBookingsView(APIView):

    @jwt_required
    def get(self, request):

        bookings = TourBooking.objects.filter(user=request.user)

        serializer = TourBookingSerializer(bookings, many=True)

        return Response(serializer.data)


class BookingDetailView(APIView):

    @jwt_required
    def get(self, request, pk):

        try:
            booking = TourBooking.objects.get(
                id=pk,
                user=request.user
            )
        except TourBooking.DoesNotExist:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TourBookingSerializer(booking)

        return Response(serializer.data)