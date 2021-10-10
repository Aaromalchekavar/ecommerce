from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('adminlogin', views.adminlogin),
    path('', views.login),
    path('logout', views.logout),
    path('adminpage', views.admin),
    path('create_user', views.create_user),
    path('display_user', views.display_user),
    path('update_user', views.update_user),
    path('delete_user', views.delete_user),
]
