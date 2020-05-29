from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from checkout.forms import OrderForm

# Create your views here.


@login_required
def checkout(request):
    order_form = OrderForm()
    return render(request, 'checkout/checkout.html', {'order_form': order_form})