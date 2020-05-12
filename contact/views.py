from django.shortcuts import render, redirect, reverse
from .forms import ContactForm

# Create your views here.


def contact(request):
    """A view that displays the Contact page"""
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})


def contact_form(request):
    """Submits detail of contact form"""
    form = ContactForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect(reverse('contact'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {'form': form})


def faq(request):
    """A view that display the Frequently Asked Questions page"""
    return render(request, "contact/faq.html")
