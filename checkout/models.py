from django.db import models
from products.models import Products

# Create your models here.

class Order(models.Model):
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    town_city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
