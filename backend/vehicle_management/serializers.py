from rest_framework import serializers
from .models import *

# Motorcycles
class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['id', 'color', 'price', 'machine', 'suspenssion_type', 'transmission_type']

class MotorcycleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['release_year', 'color', 'price', 'machine', 'suspenssion_type', 'transmission_type']
