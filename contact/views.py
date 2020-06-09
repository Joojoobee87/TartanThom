from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
from tartanthom import urls
import os

# Create your views here.


def contact(request):
    """Submits detail of contact form"""
    form = ContactForm(request.POST)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("1. I am here")
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        from_email = 'jo.broomfield87@gmail.com'
        to_email = ['jo.broomfield87@gmail.com']
        message_context = {
            'email': email,
            'message': message
        }
        html_message = render_to_string('contact/contact_message.html', message_context)
        plain_message = strip_tags(html_message)
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            print("2. I am now here")

            if subject and message and from_email:
                print("3. I am here.....")
                try:
                    print("4. I am trying....")
                    print(from_email)
                    print(to_email)
                    print(subject)
                    print(message)
                    print(html_message)
                    send_mail(subject, plain_message, from_email, to_email, html_message=html_message, fail_silently=False)
                    #send_mail(subject, message, from_email, to_email, fail_silently=False)
                    return redirect(reverse('index'))
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                except BadHeaderError:
                    print("5. I have an issue")
                    return HttpResponse('Invalid header found')
                return render(request, "home/index.html")
            else:
                form.errors
                print(form.errors)

            # if a GET (or any other method) we'll create a blank form
    else:

        form = ContactForm()

    return render(request, "contact/contact.html", {'form': form})


def faq(request):
    """A view that display the Frequently Asked Questions page"""
    return render(request, "contact/faq.html")
