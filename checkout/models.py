import uuid
from django.db.models import Sum
from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.


class Order(models.Model):
    order_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default='')
    order_number = models.CharField(max_length=32)
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    town_city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = CountryField(blank_label='Country', max_length=30)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    is_complete = models.BooleanField(default=False)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()

    def calc_order_total(self):
        self.order_total = self.lineitems.aggregate(Sum('item_total'))['item_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.create_order_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE, related_name='lineitems')
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


class Bespoke(models.Model):
    class Meta:

        verbose_name_plural = 'Bespoke'

    bespoke_order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    bespoke_product = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    person_name1 = models.CharField(max_length=50, blank=True, null=True)
    person_name2 = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=50, blank=True, null=True)
    birth_weight_lb = models.IntegerField(blank=True, null=True)
    birth_weight_oz = models.IntegerField(blank=True, null=True)
    wedding_date = models.DateField(blank=True, null=True)
    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    is_complete = models.BooleanField(default=False)
