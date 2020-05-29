from django.shortcuts import render
from checkout.forms import OrderForm

# Create your views here.


def checkout(request):
    order_form = OrderForm()
    return render(request, 'checkout/checkout.html', {'order_form': order_form})