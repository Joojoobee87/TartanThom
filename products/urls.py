from django.urls import path, re_path
from products.views import view_products, view_cards, view_cake_toppers, view_gifts, view_product


app_name = 'products'
urlpatterns = [
    path('', view_products, name='view_products'),
    path('cards/', view_cards, name='view_cards'),
    path('cake-toppers/', view_cake_toppers, name='view_cake-toppers'),
    path('gifts/', view_gifts, name='view_gifts'),
    path('view-product/<id>/', view_product, name='view_product'),
]