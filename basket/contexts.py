from django.shortcuts import get_object_or_404
from products.models import Products


def basket_contents(request):
    """Make the contents of the basket available for all pages"""

    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    product_count = 0

    for id, quantity in basket.items():
        product = get_object_or_404(Products, pk=id)
        if product.sale_price:
            total += quantity * product.sale_price
            product_count += quantity
            basket_items.append({'id': id, 'quantity': quantity, 'product': product})
        else:
            total += quantity * product.price
            product_count += quantity
            basket_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'basket_items': basket_items, 'total': total, 'product_count': product_count}
