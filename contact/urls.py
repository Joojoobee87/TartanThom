from django.urls import path
from contact.views import contact, faq

app_name = 'contact'
urlpatterns = [
    path('contactus/', contact, name='contact'),
    path('faq/', faq, name='faq'),
]
