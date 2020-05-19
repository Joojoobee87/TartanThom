from django.urls import path, re_path
from products.views import view_products, view_cards, view_cake_toppers, view_gifts, view_product


app_name = 'products'
urlpatterns = [
    path('products/', view_products, name='products'),
    path('cards/', view_cards, name='cards'),
    path('cake-toppers/', view_cake_toppers, name='cake-toppers'),
    path('gifts/', view_gifts, name='gifts'),
    path('view-product/<id>/', view_product, name='view_product'),
]