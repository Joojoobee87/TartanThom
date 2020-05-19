from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    PRODUCT_TYPE = [
        ('Cards', 'Cards'),
        ('Cake', 'Cake Toppers'),
        ('Gifts', 'Gifts')
    ]
    category = [
        ('B', 'Birthday'),
        ('W', 'Wedding'),
        ('A', 'Anniversary'),
        ('H', 'New Home'),
        ('BB', 'Baby')
    ]
    labels = [
        ('New', 'New'),
        ('Sale', 'Sale')
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5')
    ]
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPE)
    image = models.ImageField(upload_to='img')
    description = models.TextField()
    category = models.CharField(max_length=100, choices=category)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sale_price = models.DecimalField(decimal_places=2, max_digits=5)
    size = models.CharField(max_length=100, choices=sizes)
    label = models.CharField(max_length=100, choices=labels)
    tags = models.CharField(max_length=100)
    is_bespoke = models.BooleanField()
    is_active = models.BooleanField()

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.description, self.category)


class ProductReviews(models.Model):
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    user_anonymous = models.BooleanField(default=False)
    product = models.ForeignKey('Products', null=False, on_delete=models.CASCADE)
    review_text = models.TextField(null=False)
    review_rating = models.IntegerField()
    review_date = models.DateField()
    review_active = models.BooleanField(default=True)

    def review_percentage(self):
        return int((self.review_rating / 5) * 100)
