from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('adminlogin',views.adminlogin),
    path('',views.login),

]
