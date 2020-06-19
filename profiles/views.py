from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.forms import TestimonialForm, UserDetailsForm
import datetime

# Create your views here.


@login_required
def my_profile(request):
    """ Displays users profile page or redirects to login for authentication"""
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profiles/my_profile.html', context)


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


@login_required
def my_details(request):
    """ A view to render User Details and allow them to update them """
    form = UserDetailsForm(instance=request.user)
    context = {
            'form': form,
    }
    if request.method == "POST":
        form = UserDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been updated")
            return redirect(reverse('profiles:my_profile'))
        else:
            messages.error(request, "Please check your details and try again")
    return render(request, 'profiles/my_details.html', context)
