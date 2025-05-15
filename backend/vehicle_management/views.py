from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from .serializers import (
    MotorcycleCreateSerializer,
    MotorcycleUpdateSerializer,
    CarCreateSerializer,
    CarUpdateSerializer,
)
from .models import Motorcycle, Car

""" Motorcycles """
class MotorcycleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """return all of motorcycle"""
        try:
            motorcycles = [
                {
                    "id": mc.id,
                    "release_year": mc.release_year,
                    "color": mc.color,
                    "price": mc.price,
                    "stock": mc.stock,
                    "machine": mc.machine,
                    "suspenssion_type": mc.suspenssion_type,
                    "transmission_type": mc.transmission_type,
                }
                for mc in Motorcycle.objects.all()
            ]

            return Response(motorcycles, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MotorcycleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = MotorcycleCreateSerializer(data=request.data)
        if serializer.is_valid():
            motorcycle = serializer.save()
            return Response(
                {
                    "message": "Motorcycle created successfully",
                    "data": MotorcycleCreateSerializer(motorcycle).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MotorcycleUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        try:
            motorcycle = Motorcycle.objects.get(pk=pk)
        except Motorcycle.DoesNotExist:
            return Response(
                {"error": "Motorcycle not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MotorcycleUpdateSerializer(
            motorcycle, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Motorcycle updated successfully", "user": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": [serializer.errors[error][0] for error in serializer.errors]},
            status=status.HTTP_400_BAD_REQUEST,
        )


class MotorcycleDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        user = get_object_or_404(Motorcycle, pk=pk)
        user.delete()
        return Response(
            {"message": "Motorcycle deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


""" Cars """
class CarListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """return all of cars"""
        try:
            cars = [
                {
                    "id": car.id,
                    "release_year": car.release_year,
                    "color": car.color,
                    "price": car.price,
                    "stock": car.stock,
                    "machine": car.machine,
                    "passenger_cap": car.passenger_cap,
                    "type": car.type,
                }
                for car in Car.objects.all()
            ]

            return Response(cars, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CarCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CarCreateSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save()
            return Response(
                {
                    "message": "Car created successfully",
                    "data": CarCreateSerializer(car).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = CarUpdateSerializer(
            car, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Car updated successfully", "user": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": [serializer.errors[error][0] for error in serializer.errors]},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CarDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        user = get_object_or_404(Car, pk=pk)
        user.delete()
        return Response(
            {"message": "Car deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
