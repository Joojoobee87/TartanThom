from django.shortcuts import render

# Create your views here.


def index(request):
    """A view that displays the homepage"""
    return render(request, "home/index.html")
