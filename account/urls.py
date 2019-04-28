from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
]