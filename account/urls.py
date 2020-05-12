from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from account.views import user_registration, user_login, user_logout, user_account, dashboard
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', user_account, name='account'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', 
        auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('', views.dashboard, name='dashboard'),
]