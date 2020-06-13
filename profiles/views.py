from django.shortcuts import render, redirect, reverse, get_object_or_404
from checkout.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from home.forms import TestimonialForm
import datetime

# Create your views here.


@login_required
def my_profile(request):
    if request.user:
        user = request.user
        try:
            user_orders = Order.objects.filter(order_user=user).values()
            if user_orders:
                return render(request, 'profiles/my_profile.html', {'user': user, 'user_orders': user_orders})
            else:
                messages.info(request, "There are no orders")
        except:
            HttpResponseBadRequest("Something went wrong!")
            return redirect(reverse('index'))
    return render(request, 'profiles/my_profile.html', {'user': user})


@login_required
def testimonial(request):
    """"Displays testimonial page with form for user to complete and submit"""
    print("1. I am here")
    form = TestimonialForm()
    context = {
            'form': form,
    }
    if request.method == 'POST':
        print("2. I am here")
        form_data = {
            'testimonial': request.POST['testimonial'],
            'testimonial_allow_publish': request.POST['testimonial_allow_publish'],
        }
        form = TestimonialForm(form_data)
        if form.is_valid():
            print("3. I am here")
            testimonial = form.save(commit=False)
            testimonial.testimonial_date = datetime.datetime.now()
            testimonial.testimonial_user = request.user
            testimonial.save()
            messages.success(request, 'Thanks for submitting your testimonial!')
        else:
            print("4. I am here")
            messages.error(request, 'Please check the information in the form')
    else:
        print("I am not a POST")

    return render(request, 'home/testimonial.html', context)
