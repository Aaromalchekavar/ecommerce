from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

# Create your views here.


def login(req):
    if req.method == 'POST':
        username = req.POST['email']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': False},
                safe=False)
    return render(req, 'login.html')


def register(req):
    if req.method == 'POST':
        email = req.POST['email']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        password = req.POST['password']
        print(email)
        user = User.objects.create_user(
            username=email, last_name=last_name, first_name=first_name, password=password, email=email)
        user.save()
        return JsonResponse(
            {'success': True},
            safe=False)
    return render(req, 'register.html')


def adminlogin(req):
    return render(req, 'adminlogin.html')


def logout(req):
    return render(req, 'login.html')
