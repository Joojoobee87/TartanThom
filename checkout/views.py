from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from checkout.forms import OrderForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            order.date = timezone.now()
        else:
            print(order_form.errors)
            messages.error(request, "Please review your details")
    else:
        order_form = OrderForm()
    return render(request, 'checkout/checkout.html', {'order_form': order_form})