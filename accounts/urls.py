from django.urls import path, re_path
from accounts.views import user_registration, user_login, user_logout, user_account

app_name = 'accounts'
urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', user_account, name='account'),
]