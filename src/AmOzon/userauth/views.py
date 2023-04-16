from django.shortcuts import render, HttpResponseRedirect
from userauth.models import User
from userauth.forms import UserLoginForm, UserRegistrationForm, SellerLoginForm, SellerRegistrationForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Permission
from main.models import Product
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                print(user.user_permissions.all())
                auth.login(request, user)
                return HttpResponseRedirect('/')

                 
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'userauth/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            print("invalid")
    else:
        form = UserRegistrationForm()
    context = {'form' : form}
    return render(request, 'userauth/register.html', context)

def seller_login(request):
    if request.method == 'POST':
        form = SellerLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                print(user.user_permissions.all())
                auth.login(request, user)
                return HttpResponseRedirect('/')

                 
    else:
        form = SellerLoginForm()
    context = {'form': form}
    return render(request, 'userauth/seller_login.html', context)

def seller_register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            permition = Permission.objects.get(name='is_seller')
            user.user_permissions.add(permition)
            print()
            return HttpResponseRedirect(reverse('seller_login'))
        else:
            print("invalid")
    else:
        form = SellerRegistrationForm()
    context = {'form' : form}
    return render(request, 'userauth/seller_register.html', context)

def user_account(request):
    return render(request, 'userauth/user_account.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


