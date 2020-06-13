from django.shortcuts import render
from .models import Testimonials

# Create your views here.


def index(request):
    """A view that displays the homepage"""
    testimonials = Testimonials.objects.all()
    context = {
        'testimonials': testimonials,
    }
    return render(request, "home/index.html", context)
