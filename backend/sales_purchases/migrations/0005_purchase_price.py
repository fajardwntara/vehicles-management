# Generated by Django 5.2.1 on 2025-05-15 22:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_purchases', '0004_purchase_qty_sale_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
