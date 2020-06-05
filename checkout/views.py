from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from checkout.forms import OrderForm
from .models import Order, OrderItem
from products.models import Products
from basket.contexts import basket_contents
from django.utils import timezone
from django.contrib import messages
import os
import stripe

# Create your views here.


@login_required
def checkout(request):

    print("1 - Start of function")
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


def checkout_success(request):
    """Return success page on successful checkout"""
    return render(request, 'checkout/success.html')
