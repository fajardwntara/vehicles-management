from rest_framework import serializers
from .models import Sale, Purchase

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'vehicle', 'sale_date', 'buyer_name', 'buyer_phone']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'vehicle', 'purchase_date', 'seller_name', 'seller_phone']