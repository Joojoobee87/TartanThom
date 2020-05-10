from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import LoginForm, RegistrationForm

# Create your views here.


def user_registration(request):
    """Register a new user"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            if user:
                login(user=user, request=request)
                messages.success(request, "A Tartan Thom account has been created for 'f{{username}}'")
            else:
                messages.error(request, "Sorry, we were unable to register your account")
    else:
        registration_form = RegistrationForm()
    return render(request, 'accounts/register.html', {
        "registration_form": registration_form})


def user_login(request):
    login_form = LoginForm()
    """username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ..."""
    return render(request, 'accounts/login.html', {
        "login_form": login_form})


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
    # Redirect to a success page.


@login_required()
def user_account(request):
    """Users Account"""
