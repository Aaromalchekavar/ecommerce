from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.


def login(req):
    if req.method == 'POST':
        email = req.POST['email']
        password = req.POST['password']
        if email == 'test' and password == 'test':
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': False},
                safe=False)
    return render(req, 'login.html')


def register(req):
    return render(req, 'register.html')


def adminlogin(req):
    return render(req, 'adminlogin.html')
