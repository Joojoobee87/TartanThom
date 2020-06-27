import uuid
from django.db.models import Sum
from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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
    order_total = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    delivery_total = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    grand_total = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    is_complete = models.BooleanField(default=False)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.create_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """
        Update order total, delivery and grand total as line items
        are added, updated or deleted
        """
        self.order_total = self.lineitems.aggregate(
            Sum('item_total'))['item_total__sum'] or 0
        if self.order_total < settings.MIN_DELIVERY_THRESHOLD:
            self.delivery_total = settings.MIN_DELIVERY_CHARGE
        else:
            self.delivery_total = settings.UPPER_DELIVERY_CHARGE
        self.grand_total = float(self.order_total) + float(self.delivery_total)
        self.save()

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
    is_complete = models.BooleanField(blank=True, default=False)


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
