from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0),
                                                                  MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100, default="processing")
    date_created_order = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)









