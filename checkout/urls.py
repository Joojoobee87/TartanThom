from django.urls import path
from checkout.views import checkout, checkout_success
from .webhooks import webhook

app_name = 'checkout'
urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/<order_number>/', checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]