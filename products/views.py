from django.shortcuts import render, get_object_or_404
from products.models import Products, ProductReviews
import datetime

# Create your views here.


def view_products(request):
    """View all products in the collection"""
    products = Products.objects.all()
    product_type = "All Products"
    return render(request, "products/products.html", {'products': products, 'product_type': product_type})


def view_cards(request):
    """View all products with the product type 'Cards' """
    products = Products.objects.filter(product_type='Cards')
    product_type = "Cards"
    return render(request, "products/products.html", {'products': products, 'product_type': product_type})


def view_cake_toppers(request):
    """View all products with the product type 'Cake Toppers' """
    products = Products.objects.filter(product_type='Cake Toppers')
    product_type = "Cake Toppers"
    return render(request, "products/products.html", {'products': products, 'product_type': product_type})


def view_gifts(request):
    """View all products with the product type 'Gifts' """
    products = Products.objects.filter(product_type='Gifts')
    product_type = "Gifts"
    return render(request, "products/products.html", {'products': products, 'product_type': product_type})


def view_product(request, id):
    """View selected product in the collection"""
    product = get_object_or_404(Products, pk=id)
    reviews = ProductReviews.objects.filter(product=id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, "products/product.html", context)


def review_product(request, id):
    """ Review form for user to submit for a specific product"""
    print("1. I am here")
    form = ReviewForm()
    context = {
            'form': form,
    }
    product = get_object_or_404(Products, pk=id)
    if request.method == 'POST':
        print("2. I am here")
        form_data = {
            'review_rating': request.POST['review_rating'],
            'review_text': request.POST['review_text'],
            'user_anonymous': request.POST['user_anonymous'],
        }
        form = ReviewForm(form_data)
        if form.is_valid():
            print("3. I am here")
            review = form.save(commit=False)
            review.review_date = datetime.datetime.now()
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Thanks for submitting your review!')
        else:
            print("4. I am here")
            messages.error(request, 'Please check the information in the form')
    else:
        print("I am not a POST")

    return render(request, 'products/review_product.html', context)
