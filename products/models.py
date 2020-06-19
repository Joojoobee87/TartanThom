from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):

    class Meta:

        verbose_name_plural = 'Products'

    PRODUCT_TYPE = [
        ('cards', 'Cards'),
        ('cake-toppers', 'Cake-Toppers'),
        ('gifts', 'Gifts')
    ]
    category = [
        ('Birthday', 'Birthday'),
        ('Wedding', 'Wedding'),
        ('Anniversary', 'Anniversary'),
        ('New Home', 'New Home'),
        ('Baby', 'Baby')
    ]
    labels = [
        ('New', 'New'),
        ('Sale', 'Sale')
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('200mm x 200mm', '200mm x 200mm'),
        ('122mm x 172mm', '122mm x 172mm'),
        ('172mm x 122mm', '172mm x 122mm'),
        ('250mm x 250mm', '250mm x 250mm'),
        ('210mm x 297mm', '210mm x 297mm'),
        ('152mm x variable', '152mm x variable'),
    ]
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPE)
    image = models.ImageField(upload_to='img', default='static/img/TartanThomDefault.jpg')
    description = models.TextField()
    category = models.CharField(max_length=100, choices=category)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sale_price = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    size = models.CharField(max_length=100, choices=sizes)
    label = models.CharField(blank=True, max_length=100, choices=labels)
    tags = models.CharField(blank=True, max_length=100)
    is_bespoke = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductReviews(models.Model):

    class Meta:

        verbose_name_plural = 'Product Reviews'

    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    user_anonymous = models.BooleanField(default=False)
    product = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    review_text = models.TextField(null=False, max_length=500)
    review_rating = models.IntegerField(null=False, default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_date = models.DateField(auto_now_add=True)
    review_active = models.BooleanField(default=True)

    def __str__(self):

        return self.user.username

    def review_percentage(self):
        return int((self.review_rating / 5) * 100)
