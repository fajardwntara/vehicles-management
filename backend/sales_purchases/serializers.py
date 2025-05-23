from rest_framework import serializers
from .models import Sale, Purchase
from vehicle_management.models import Vehicle

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    """ Reduce the stock when canceling the vehicle's sale """
    def update(self, instance, validated_data):

        previous_status = instance.status
        new_status = validated_data.get('status', previous_status)
        vehicle = validated_data.get('vehicle', instance.vehicle)
        qty = instance.qty

        if previous_status == 'confirm' and new_status != 'cancel':
            raise serializers.ValidationError("Data with status 'confirm' cannot be updated. Only can be canceled.")

        if previous_status == 'cancel':
            raise serializers.ValidationError("Data with status 'cancel' cannot be updated.")

        if previous_status != new_status and new_status in ['cancel', 'confirm']:
            vehicle.stock += qty if new_status == 'cancel' else -qty
            vehicle.save()

        return super().update(instance, validated_data)

class PurchaseSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all()) 

    class Meta:
        model = Purchase
        fields = '__all__'

    def update(self, instance, validated_data):
        previous_status = instance.status
        new_status = validated_data.get('status', previous_status)
        vehicle = validated_data.get('vehicle_id', instance.vehicle)
        qty = instance.qty

        if previous_status == 'confirm' and new_status != 'cancel':
            raise serializers.ValidationError("Data with status 'confirm' cannot be updated. Only can be canceled.")

        if previous_status == 'cancel':
            raise serializers.ValidationError("Data with status 'cancel' cannot be updated.")

        if previous_status != 'confirm' and new_status == 'confirm':
            if vehicle.stock < qty:
                raise serializers.ValidationError(f"Insufficient stock. Available stock: {vehicle.stock}")

            vehicle.stock -= qty
            vehicle.save()

        elif previous_status == 'confirm' and new_status == 'cancel':
            vehicle.stock += qty
            vehicle.save()

        return super().update(instance, validated_data)