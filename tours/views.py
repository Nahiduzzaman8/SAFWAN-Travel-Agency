from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TourPackage
from .serializers import TourPackageSerializer
from accounts.decorators import jwt_required

class TourListView(APIView):
    @jwt_required
    def get(self, request):
        tours = TourPackage.objects.all()
        serializer = TourPackageSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TourDetailView(APIView):
    @jwt_required
    def get(self, request, pk):
        try:
            tour = TourPackage.objects.get(pk=pk)
        except TourPackage.DoesNotExist:
            return Response({"error": "Tour not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TourPackageSerializer(tour)
        return Response(serializer.data, status=status.HTTP_200_OK)
