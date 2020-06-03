from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from checkout.forms import OrderForm
from django.utils import timezone
from django.contrib import messages
import os

# Create your views here.


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            order.date = timezone.now()
            print(order_form.errors)
            messages.success(request, "Thank you for your order")
            return redirect(request, 'products')
        else:
            print(order_form.errors)
            messages.error(request, "Please review your details")
    else:
        order_form = OrderForm()
        context = {
            'order_form': order_form,
            'stripe_public_key': os.environ.get('STRIPE_PUBLISHABLE'),
            'client_secret': os.environ.get('STRIPE_SECRET'),
        }

    return render(request, 'checkout/checkout.html', context)
