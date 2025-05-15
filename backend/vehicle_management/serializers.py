from rest_framework import serializers
from .models import *

# Motorcycles
class MotorcycleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['id', 'release_year', 'color', 'price', 'stock', 'machine', 'suspenssion_type', 'transmission_type']

class MotorcycleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['id', 'release_year', 'color', 'price', 'stock', 'machine', 'suspenssion_type', 'transmission_type']


# Cars
class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['release_year', 'color', 'price', 'stock', 'machine', 'passenger_cap', 'type']

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'release_year', 'color', 'price', 'stock', 'machine', 'passenger_cap', 'type']

