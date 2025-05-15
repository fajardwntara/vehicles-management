from django.db import models
from vehicle_management.models import Vehicle

class Sale(models.Model):
    STATUS_CHOICES = (
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateField()
    buyer_name = models.CharField(max_length=100, null=True)
    buyer_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirm')

    def __str__(self):
        return f"Sale of {self.vehicle} to {self.buyer_name} on {self.sale_date} ({self.status})"


class Purchase(models.Model):
    STATUS_CHOICES = (
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateField()
    seller_name = models.CharField(max_length=100, null=True)
    seller_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirm')

    def __str__(self):
        return f"Purchase of {self.vehicle} from {self.seller_name} on {self.purchase_date} ({self.status})"
