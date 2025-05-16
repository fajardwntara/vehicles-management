from django.db import models
from vehicle_management.models import Vehicle
from django.core.validators import MinValueValidator

STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    )
class Sale(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateField()
    buyer_name = models.CharField(max_length=100, null=True)
    buyer_phone = models.CharField(max_length=20)
    qty = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"Sale of {self.vehicle} to {self.buyer_name} on {self.sale_date} ({self.status})"


class Purchase(models.Model):
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateField()
    seller_name = models.CharField(max_length=100, null=True)
    seller_phone = models.CharField(max_length=20)
    qty = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    purchase_price = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        return f"Purchase of {self.vehicle} from {self.purchase_price} on {self.purchase_date} ({self.status})"
