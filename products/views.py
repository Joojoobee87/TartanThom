from django.shortcuts import render, get_object_or_404
from products.models import Products, ProductReviews

# Create your views here.


def view_products(request):
    """View all products in the collection"""
    products = Products.objects.all()
    return render(request, "products/products.html", {'products': products})


def view_cards(request):
    """View all products with the product type 'Cards' """
    products = Products.objects.filter(product_type='Cards')
    return render(request, "products/products.html", {'products': products})


def view_cake_toppers(request):
    """View all products with the product type 'Cake Toppers' """
    products = Products.objects.filter(product_type='Cake Toppers')
    return render(request, "products/products.html", {'products': products})


def view_gifts(request):
    """View all products with the product type 'Gifts' """
    products = Products.objects.filter(product_type='Gifts')
    return render(request, "products/products.html", {'products': products})


def view_product(request, id):
    """View selected product in the collection"""
    product = get_object_or_404(Products, pk=id)
    reviews = ProductReviews.objects.filter(product=id)
    return render(request, "products/product.html", {
        'product': product, 'reviews': reviews})
