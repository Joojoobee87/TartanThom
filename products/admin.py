from django.contrib import admin
from .models import Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name', 'category', 'price', 'is_active')


admin.site.register(Products, ProductsAdmin)
