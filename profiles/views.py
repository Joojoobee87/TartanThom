from django.shortcuts import render, redirect, reverse, get_object_or_404
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

# Create your views here.


@login_required
def my_profile(request):
    print("1. My Profile")
    if request.user:
        print("2. I have a user")
        user = request.user
        print(user)
        print(user.id)
        try:
            print("3. I am trying")
            user_orders = Order.objects.filter(order_user=user).values()
            print(user_orders)
            if user_orders:
                print("3. My user has orders")
                return render(request, 'profiles/my_profile.html', {'user': user, 'user_orders': user_orders})
            else:
                print("No orders")
        except:
            HttpResponseBadRequest("Something went wrong!")
            print("4. Sorry this user has no orders")
            return redirect(reverse('index'))
    return render(request, 'profiles/my_profile.html', {'user': user})
