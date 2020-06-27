from django.shortcuts import render
from .models import Testimonials
from products.models import Products

# Create your views here.


def index(request):
    """A view that displays the homepage"""
    testimonials = Testimonials.objects.all()
    products = Products.objects.all()
    context = {
        'testimonials': testimonials,
        'products': products,
    }
    return render(request, "home/index.html", context)
