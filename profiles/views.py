from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.forms import TestimonialForm
from profiles.forms import UserDetailsForm
import datetime

# Create your views here.


@login_required
def my_profile(request):
    """
    Displays users profile page or redirects to login for authentication
    """
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profiles/my_profile.html', context)


@login_required
def testimonial(request):
    """"
    Displays testimonial page with form for user to complete and submit
    """
    form = TestimonialForm()
    context = {
            'form': form,
    }
    if request.method == 'POST':
        form_data = {
            'testimonial': request.POST['testimonial'],
            'testimonial_allow_publish': request.POST.get('testimonial_allow_publish', False),
        }
        form = TestimonialForm(form_data)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.testimonial_date = datetime.datetime.now()
            testimonial.testimonial_user = request.user
            testimonial.save()
            messages.success(request, 'Thanks for submitting your testimonial!')
            return redirect(reverse('profiles:my_profile'))
        else:
            messages.error(request, 'Please check the information in the form')
    return render(request, 'home/testimonial.html', context)


@login_required
def my_details(request):
    """
    A view to display User details and allow them to update their information
    """
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
