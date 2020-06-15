from django.urls import path
from .views import my_profile, my_details

app_name = 'profiles'
urlpatterns = [
    path('', my_profile, name='my_profile'),
    path('my_details/', my_details, name='my_details')
]
