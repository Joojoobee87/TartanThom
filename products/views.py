from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Products, ProductReviews
from products.forms import ReviewForm
from basket.forms import QuantityForm
import datetime

# Create your views here.


def view_products(request):
    """View all products in the collection"""
    products = Products.objects.all()
    product_type = "All Products"
    results_count = products.count()
    context = {
        'products': products,
        'product_type': product_type,
        'results_count': results_count,
    }
    return render(request, "products/products.html", context)


def view_products_by_type(request, product_type):
    """View all products with the product type 'Cards' """
    if request.method == 'GET':
        products = Products.objects.filter(product_type=product_type)
        results_count = products.count()
        context = {
            'products': products,
            'product_type': product_type,
            'results_count': results_count,
        }
    else:
        messages.error(request, "Sorry, there are no products of this type")
        return redirect(reverse('view_products'))
    return render(request, "products/products.html", context)


def view_product(request, id):
    """View selected product in the collection"""
    form = QuantityForm()
    product = get_object_or_404(Products, pk=id)
    reviews = ProductReviews.objects.filter(product=id)
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, "products/product.html", context)


def review_product(request, id):
    """ Review form for user to submit for a specific product"""
    form = ReviewForm()
    product = get_object_or_404(Products, pk=id)
    context = {
            'form': form,
            'product': product,
    }

    if request.method == 'POST':
        form_data = {
            'review_rating': request.POST['review_rating'],
            'review_text': request.POST['review_text'],
            'user_anonymous': request.POST.get('user_anonymous', False)
        }
        form = ReviewForm(form_data)
        if form.is_valid():
            review = form.save(commit=False)
            review.review_date = datetime.datetime.now()
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Thanks for submitting your review!')
            return redirect(reverse('profiles:my_profile'))
        else:
            messages.error(request, 'Please check the information in the form')
    else:
        print("I am not a POST")

    return render(request, 'products/review_product.html', context)
