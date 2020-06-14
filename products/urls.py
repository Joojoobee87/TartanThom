from django.urls import path, re_path
from products.views import view_products, view_products_by_type, view_product, review_product


app_name = 'products'
urlpatterns = [
    path('', view_products, name='view_products'),
    path('products_by_type/<product_type>/', view_products_by_type, name='view_products_by_type'),
    path('view-product/<id>/', view_product, name='view_product'),
    path('review-product/<id>/', review_product, name='review_product'),
]