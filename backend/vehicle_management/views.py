from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import MotorcycleSerializer, MotorcycleCreateSerializer
from .models import Motorcycle
class MotorcycleView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        motorcycle = request.motorcycle
        serializer = MotorcycleSerializer(motorcycle)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MotorcycleListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        """ return all of motorcycle """
        try:
            motorcycle = [{
                "id": mc.id,
                "color": mc.color,
                "price": mc.price,
                "machine": mc.machine,
                "suspenssion_type": mc.suspenssion_type,
                "transmission_type": mc.transmission_type,
            } for mc in Motorcycle.objects.all()]

            return Response(motorcycle, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": f"{str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class MotorcycleCreateView(APIView):
    permission_classes = [IsAuthenticated] 
    def post(self, request, format=None):
        serializer = MotorcycleCreateSerializer(data=request.data)
        if serializer.is_valid():
            motorcycle = serializer.save()
            return Response({
                "message": "Motorcycle created successfully",
                "motorcycle": MotorcycleCreateSerializer(motorcycle).data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
