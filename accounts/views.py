from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

from ecommerce.models import Order
from .models import Product, Category
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(req):
    if req.method == 'POST':
        username = req.POST['email']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            req.session['username'] = username
            req.session['password'] = password
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
    return render(req, 'adminlogin.html')

@login_required(login_url='/login')
def logout(req):
    auth.logout(req)
    return render(req, 'login.html')

@login_required(login_url='/adminlogin')
def admin(req):
    return render(req, 'admin.html')

@login_required(login_url='/adminlogin')
def create_user(req):
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
    return render(req, 'create_user.html')

@login_required(login_url='/adminlogin')
def delete_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        u = User.objects.get(username=username)
        if u is not None:
            u.delete()
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': True},
                safe=False)
    return render(req, 'delete_user.html')

@login_required(login_url='/adminlogin')
def update_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        u = User.objects.get(username=username)
        if u is not None:
            if email != '':
                u.username = email
            if first_name != '':
                u.first_name = first_name
            if last_name != '':
                u.last_name = last_name
            u.save()
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': True},
                safe=False)
    return render(req, 'update_user.html')

@login_required(login_url='/adminlogin')
def display_user(req):
    users = User.objects.all()
    return render(req, 'display_user.html', {'users': users})

@login_required(login_url='/adminlogin')
def add_category(req):
    if req.method == 'POST':
        category = req.POST['category']
        cat = Category.objects.create(name=category)
        cat.save()
        return JsonResponse(
            {'success': True},
            safe=False)
    return render(req, 'add_category.html')

@login_required(login_url='/adminlogin')
def update_category(req):
    if req.method == 'POST':
        category = req.POST['category']
        newcategory = req.POST['newcategory']
        c = Category.objects.get(name=category)
        if c is not None:
            c.name = newcategory
            c.save()
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': True},
                safe=False)
    return render(req, 'update_category.html')

@login_required(login_url='/adminlogin')
def display_category(req):
    category = Category.objects.all()
    return render(req, 'display_category.html', {'categories': category})

@login_required(login_url='/adminlogin')
def delete_category(req):
    if req.method == 'POST':
        category = req.POST['category']
        c = Category.objects.get(name=category)
        if c is not None:
            c.delete()
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': True},
                safe=False)
    return render(req, 'delete_category.html')

@login_required(login_url='/adminlogin')
def add_product(req):

    if req.method == 'POST':
        form = ProductForm(req.POST, req.FILES)
  
        if form.is_valid():
            form.save()

        return redirect('/adminpage')
    form = ProductForm()
    return render(req, 'add_product.html', {'form' : form})

@login_required(login_url='/adminlogin')
def delete_product(req):
    if req.method == 'POST':
        name = req.POST['product']
        p = Product.objects.get(name=name)
        if p is not None:
            p.delete()
            return JsonResponse(
                {'success': True},
                safe=False)
        else:
            return JsonResponse(
                {'success': True},
                safe=False)
    return render(req, 'delete_product.html')

@login_required(login_url='/adminlogin')
def update_product(req):
    if req.method == 'POST':
        prodname = req.POST['prodname']
        name = req.POST['name']
        quantity = req.POST['quantity']
        category = req.POST['category']
        price = req.POST['price']
        description = req.POST['description']
        p = Product.objects.get(name=prodname)
        if p is not None:
            if name != '':
                p.name = name
            if name != '':
                p.quantity = quantity
            if category != '':
                p.category_id = category
            if price != '':
                p.price = price
            if description != '':
                p.description = description
            p.save()
        return JsonResponse(
            {'success': True},
            safe=False)
    cat = Category.objects.all()
    return render(req, 'update_product.html', {'categories': cat})

@login_required(login_url='/adminlogin')
def display_product(req):
    product = Product.objects.all()
    return render(req, 'display_product.html', {'products': product})

@login_required(login_url='/adminlogin')
def placed_orders(req):
    order = Order.objects.all()
    return render(req,"placed_orders.html",{"orders":order})