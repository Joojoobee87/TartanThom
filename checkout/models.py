import uuid
from django.db import models
from products.models import Products

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32)
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    town_city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.create_order_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    item_total = models.DecimalField(max_digits=8, decimal_places=2, null=False,blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Calculate total of order item """
        if not self.product.sale_price:
            self.item_total = self.product.price * self.quantity
        else:
            self.item_total = self.product.sale_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
