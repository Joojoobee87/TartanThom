from django.urls import path
from profiles.views import testimonial

app_name = 'home'
urlpatterns = [
    path('testimonial/', testimonial, name='testimonial'),
]
