from atexit import register
from django import views
from django.urls import path
from .views import register,LoginView

urlpatterns = [ 
    path('register',register.as_view(),name='register'),
    path('Login',LoginView.as_view(),name='Login'),
]