from django.urls import path
from checkout.views import checkout, checkout_success, checkout_history, order_detail
from .webhooks import webhook

app_name = 'checkout'
urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/<order_number>/', checkout_success, name='checkout_success'),
    path('checkout_history/', checkout_history, name='checkout_history'),
    path('order_detail/<order_number>', order_detail, name='order_detail'),
    path('wh/', webhook, name='webhook'),
]