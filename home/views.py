from django.shortcuts import render
from .models import Testimonials
from products.models import Products

# Create your views here.


def index(request):
    """A view that displays the homepage"""
    all_testimonials = Testimonials.objects.all()
    products = Products.objects.all()
    if all_testimonials:
        testimonials = all_testimonials
    else:
        testimonials = "We don't currently have any testimonials"

    context = {
        'testimonials': testimonials,
        'products': products,
    }
    return render(request, "home/index.html", context)
