from django.urls import path
from checkout.views import checkout

app_name = 'checkout'
urlpatterns = [
    path('', checkout, name='checkout')
]