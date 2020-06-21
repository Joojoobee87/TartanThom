from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from checkout.forms import OrderForm, BespokeForm
from .models import Order, OrderItem
from products.models import Products
from basket.contexts import basket_contents
from django.contrib import messages
import stripe

# Create your views here.


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'fullname': request.POST['fullname'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_city': request.POST['town_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.order_user = request.user
            order.save()
            for id, quantity in basket.items():
                try:
                    product = Products.objects.get(pk=id)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    order_item.save()
                    del request.session['basket']
                    del request.session['product_count']
                    request.session.modified = True
                except Products.DoesNotExist:
                    order.delete()
            return redirect(reverse('checkout:checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "I'm sorry, there seems to be a problem ordering at this time. Please try again later")
    else:
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


@login_required
def checkout_success(request, order_number):
    """Return success page on successful checkout showing order detail"""
    order = get_object_or_404(Order, order_number=order_number)

    return render(request, 'checkout/success.html', {'order': order})


@login_required
def checkout_history(request):
    """ Returns a list of previous orders for the logged in user """
    user = request.user
    user_orders = Order.objects.filter(order_user=user).order_by('-date')
    if user_orders:
        context = {
            'user_orders': user_orders,
        }
    else:
        messages.error("Sorry, you don't currently have any orders")
        return redirect(reverse('profiles:my_profile'))

    return render(request, 'checkout/checkout_history.html', context)


@login_required
def order_detail(request, order_number):
    """Return details of an individual order and the items within the order"""
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
    }
    return render(request, 'checkout/order_detail.html', context)


def bespoke(request, order_number, id):
    """
    Returns a bespoke form for users to complete further
    information for order items
    """
    form = BespokeForm()
    product = get_object_or_404(Products, pk=id)
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'form': form,
        'order': order,
        'product': product,
    }
    if request.method == 'POST':
        form = BespokeForm(request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            bespoke = form.save(commit=False)
            bespoke.bespoke_order = order
            bespoke.bespoke_product = product
            bespoke.save()
            messages.success(request, 'Thanks for submitting your bespoke details!')
        else:
            messages.error(request, '%s - Please check the information in the form' %form.errors )

    return render(request, 'checkout/bespoke.html', context)
