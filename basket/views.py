from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_basket(request):
    """A view that renders the contents of the basket"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, id):
    """A view that adds the quantity of a product to the basket"""
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if id in basket:
        basket[id] = int(basket[id]) + quantity
    else:
        basket[id] = basket.get(id, quantity)

    request.session['basket'] = basket
    return render(request, 'basket/basket.html')


def amend_basket(request, id):
    """A view that amends the quantity of a product in the basket"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop[id]
    return render(request, 'basket/basket.html')


def delete_from_basket(request, id):
    """A view that deletes the specified item from the basket"""
    basket = request.session.get('basket', {})
    del basket[id]
    return render(request, 'basket/basket.html')
