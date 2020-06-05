from django.urls import path
from checkout.views import checkout, checkout_success

app_name = 'checkout'
urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/', checkout_success, name='checkout_success')
]