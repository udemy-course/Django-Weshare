from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='account/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='account/logout.html'
        ),
        name='logout'
    ),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='account/password_change.html'
        ),
        name='password_change'
    ),
    path(
        'password-change-done',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.html'
        ),
        name='password_change_done'
    )
]