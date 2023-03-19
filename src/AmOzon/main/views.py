from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'products' : Product.objects.all()})

def details(request):
    return render(request, 'main/details.html')
