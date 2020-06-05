from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from checkout.forms import OrderForm
from basket.contexts import basket_contents
from django.utils import timezone
from django.contrib import messages
import os
import stripe

# Create your views here.


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    basket = request.session.get('basket', {})
    current_contents = basket_contents(request)
    total = current_contents['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    order_form = OrderForm()
    
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


    
    """if request.method == "POST":
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

    return render(request, 'checkout/checkout.html', context)"""
