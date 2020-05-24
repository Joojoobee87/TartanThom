from django.urls import path
from .views import view_basket, add_to_basket, amend_basket, delete_from_basket


app_name = 'basket'
urlpatterns = [
    path('', view_basket, name='view_basket'),
    path('add/<id>/', add_to_basket, name='add_to_basket'),
    path('amend/<id>/', amend_basket, name='amend_basket'),
    path('delete/<id>/', delete_from_basket, name='delete_from_basket'),
]
