from django.contrib import admin
from .models import Products, ProductReviews

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name', 'category', 'price', 'is_active')


class ProductReviewsAdmin(admin.ModelAdmin):
    model = ProductReviews
    list_display = ('user', 'review_date', 'review_active')


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
