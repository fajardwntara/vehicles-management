from django.db import models
from django.core.validators import MinValueValidator

class Vehicle(models.Model):
    
    release_year = models.IntegerField(
        validators=[MinValueValidator(1900)]
    )
    color = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.color} - {self.release_year} - {self.price}"

class Motorcycle(Vehicle):
    
    machine = models.CharField(max_length=100)
    suspenssion_type = models.CharField(max_length=100)
    transmission_type = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Motorcycle'
        verbose_name_plural = 'Motorcycles'
    
    def __str__(self):
        return f"{self.uuid} - {self.machine}"

class Car(Vehicle):
    
    machine = models.CharField(max_length=100)
    passenger_cap = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
    
    def __str__(self):
        return f"{self.uuid} - {self.type} ({self.passenger_cap} passengers)"