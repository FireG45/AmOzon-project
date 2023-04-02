from django.shortcuts import render, HttpResponseRedirect
from userauth.models import User
from userauth.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
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
        form = UserRegistrationForm()
    context = {'form' : form}
    return render(request, 'userauth/register.html', context)


