from rest_framework import serializers
from .models import *

# Motorcycles
class MotorcycleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = '__all__'

class MotorcycleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = '__all__'


# Cars
class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
