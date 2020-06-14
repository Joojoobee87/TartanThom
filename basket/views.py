from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import QuantityForm
from django.contrib import messages

# Create your views here.


def view_basket(request):
    """A view that renders the contents of the basket"""
    form = QuantityForm()
    context = {
        'form': form,
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, id):
    """A view that adds the quantity of a product to the basket"""
    form = QuantityForm()
    context = {
        'form': form,
    }
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if request.method == "POST":
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST['quantity'])
            if id in basket:
                basket[id] = int(basket[id]) + quantity
            else:
                basket[id] = basket.get(id, quantity)
        else:
            form = QuantityForm()
            messages.error(request, "Please enter a value to update quantity")
            return redirect(reverse('basket:view_basket'))

    request.session['basket'] = basket
    return render(request, 'basket/basket.html', context)


def amend_basket(request, id):
    """A view that amends the quantity of a product in the basket"""
    basket = request.session.get('basket', {})
    form = QuantityForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST['quantity'])
            basket = request.session.get('basket', {})
            if quantity > 0:
                basket[id] = quantity
            else:
                basket.pop[id]
            request.session.modified = True
        else:
            form = QuantityForm()
            messages.error(request, "Please enter a value to update quantity")
            return redirect(reverse('basket:view_basket'))

    return render(request, 'basket/basket.html', context)


def delete_from_basket(request, id):
    """A view that deletes the specified item from the basket"""
    basket = request.session.get('basket', {})
    del basket[id]
    if not basket.items():
        request.session['product_count'] = 0
    request.session.modified = True
    return render(request, 'basket/basket.html')
