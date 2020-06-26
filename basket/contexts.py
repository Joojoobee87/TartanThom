from django.shortcuts import get_object_or_404
from products.models import Products
from django.conf import settings
from decimal import Decimal


def basket_contents(request):
    """Make the contents of the basket available for all pages"""

    basket = request.session.get('basket', {})

    basket_items = []
    order_total = 0
    product_count = 0

    for id, quantity in basket.items():
        product = get_object_or_404(Products, pk=id)
        if product.sale_price:
            order_total += quantity * product.sale_price
            product_count += quantity
            request.session['product_count'] = product_count
            basket_items.append({
                'id': id,
                'quantity': quantity,
                'product': product
                })
        else:
            order_total += quantity * product.price
            product_count += quantity
            request.session['product_count'] = product_count
            basket_items.append({
                'id': id,
                'quantity': quantity,
                'product': product
                })

    if order_total < settings.MIN_DELIVERY_THRESHOLD:
        delivery_total = round(Decimal(settings.MIN_DELIVERY_CHARGE), 2)
    else:
        delivery_total = round(Decimal(settings.UPPER_DELIVERY_CHARGE), 2)

    grand_total = delivery_total + order_total

    context = {
        'basket_items': basket_items,
        'order_total': order_total,
        'delivery_total': delivery_total,
        'grand_total': grand_total,
        'product_count': product_count,
    }
    return context
