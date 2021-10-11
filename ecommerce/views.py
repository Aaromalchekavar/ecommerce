from django.shortcuts import render, redirect
from accounts.models import Product

def home(req):
    product = Product.objects.all()
    return render(req, 'home.html',{'products':product})
