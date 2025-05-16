from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Sale, Purchase
from .serializers import SaleSerializer, PurchaseSerializer
from vehicle_management.models import Vehicle, Car, Motorcycle

# --- SALE ---
class SaleListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """return all of data"""
        try:
            sales = [
                {
                    "id": sale.id,
                    "vehicle": sale.vehicle,
                    "sale_date": sale.sale_date,
                    "buyer_name": sale.buyer_name,
                    "buyer_phone": sale.buyer_phone,
                    "status": sale.status,
                }
                for sale in Sale.objects.all()
            ]

            return Response(sales, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class SaleCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sale created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Sale updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- PURCHASE ---
class PurchaseListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """Return all purchase data with detailed vehicle information"""
        try:
            purchases = []

            for purchase in Purchase.objects.select_related('vehicle').all():
                vehicle = purchase.vehicle
                vehicle_type = "Vehicle"
                extra_data = {}

                if Car.objects.filter(id=vehicle.id).exists():
                    car = Car.objects.get(id=vehicle.id)
                    vehicle_type = "Car"
                    extra_data = {
                        "machine": car.machine,
                        "passenger_cap": car.passenger_cap,
                        "type": car.type,
                    }
                elif Motorcycle.objects.filter(id=vehicle.id).exists():
                    motorcycle = Motorcycle.objects.get(id=vehicle.id)
                    vehicle_type = "Motorcycle"
                    extra_data = {
                        "machine": motorcycle.machine,
                        "suspenssion_type": motorcycle.suspenssion_type,
                        "transmission_type": motorcycle.transmission_type,
                    }

                purchases.append({
                    "id": purchase.id,
                    "vehicle_id": vehicle.id,
                    "vehicle_type": vehicle_type,
                    "color": vehicle.color,
                    "release_year": vehicle.release_year,
                    **extra_data,
                    "purchase_date": purchase.purchase_date,
                    "seller_name": purchase.seller_name,
                    "seller_phone": purchase.seller_phone,
                    "qty": purchase.qty,
                    "purchase_price": purchase.price,
                    "status": purchase.status,
                })

            return Response(purchases, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class PurchaseCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Purchase created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Purchase updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)