from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import SaleSerializer, PurchaseSerializer

class SaleCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sale created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Purchase created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
