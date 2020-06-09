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
    """
    Gets detail from users contact form and sends to Tartan Thom an email rendering content of form
    """
    form = ContactForm(request.POST)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        from_email = 'jo.broomfield87@gmail.com'
        to_email = ['jo.broomfield87@gmail.com']
        message_context = {
            'email': email,
            'message': message,
            'subject': subject
        }
        header = "You've got mail!"
        html_message = render_to_string('contact/contact_message.html', message_context)
        plain_message = strip_tags(html_message)
        if form.is_valid():
            if subject and message and from_email:
                try:
                    send_mail(header, plain_message, from_email, to_email, html_message=html_message, fail_silently=False)
                    return redirect(reverse('index'))
                except BadHeaderError:
                    return HttpResponse('Invalid header found')
                return render(request, "home/index.html")
            else:
                form.errors
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {'form': form})


def faq(request):
    """A view that display the Frequently Asked Questions page"""
    return render(request, "contact/faq.html")
