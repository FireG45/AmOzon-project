from django.shortcuts import render, HttpResponseRedirect
from userauth.models import User
from userauth.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

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
            user = User.objects.get(username=request.POST["username"])            
            group = Group.objects.get(name='Customer') 
            user.groups.clear()
            user.groups.add(group)

            return HttpResponseRedirect(reverse('login'))
        else:
            print("invalid")
    else:
        form = UserRegistrationForm()
    context = {'form' : form}
    return render(request, 'userauth/register.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


