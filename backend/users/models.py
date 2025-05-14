from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    token = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"