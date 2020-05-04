from django.shortcuts import render

# Create your views here.


def contact(request):
    """A view that display the Contact page"""
    return render(request, "contact/contact.html")


def faq(request):
    """A view that display the Frequently Asked Questions page"""
    return render(request, "contact/faq.html")
