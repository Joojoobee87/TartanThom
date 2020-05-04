from django.shortcuts import render

# Create your views here.


def about(request):
    """A view that display the About page"""
    return render(request, "about/about.html")


def about_design(request):
    """A view that display the Design & Craft page"""
    return render(request, "about/about_design.html")


def about_philosophy(request):
    """A view that display the Philosophy page"""
    return render(request, "about/about_philosophy.html")

