from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DistanceSerializer
import math


class DistanceView(APIView):
    def post(self, request):
        serializer = DistanceSerializer(data=request.data)
        if serializer.is_valid():
            latitude1 = serializer.validated_data['latitude1']
            longitude1 = serializer.validated_data['longitude1']
            latitude2 = serializer.validated_data['latitude2']
            longitude2 = serializer.validated_data['longitude2']

            distance = math.sqrt((latitude2 - latitude1) ** 2 + (longitude2 - longitude1) ** 2)

            return Response({'distance': distance})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
