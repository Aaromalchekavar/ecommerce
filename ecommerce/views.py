from django.shortcuts import render, redirect
from accounts.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import JsonResponse


@login_required(login_url='/login')
def home(req):
    if req.method == 'POST':
        id = req.POST['id']
        quantity = req.POST['maxQuantity']
        p = Product.objects.get(id=id)
        p.quantity = quantity
        p.save()
        return JsonResponse(
                {'success': True},
                safe=False)
    product = Product.objects.all()
    return render(req, 'home.html', {'products': product})


@login_required(login_url='/login')
def profile(req):
    if req.method == 'POST':
        username = req.session['username']
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
    if req.session.has_key('username'):
        username = req.session['username']
        u = User.objects.get(username=username)
        print(u.first_name)
        if u is not None:
            first_name = u.first_name
            email = u.email
            last_name = u.last_name
            return render(req, 'profile.html', {'fname': first_name, 'lname': last_name, 'email': email})
    return redirect('/home')


@login_required(login_url='/login')
def edit_profile(req):
    if req.method == 'POST':
        username = req.session['username']
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
    return render(req, 'edit_profile.html')
