from django.urls import path
from about.views import about, about_design, about_philosophy

app_name = 'about'
urlpatterns = [
    path('', about, name='about'),
    path('design/', about_design, name='about_design'),
    path('philosophy/', about_philosophy, name='about_philosophy'),
]
