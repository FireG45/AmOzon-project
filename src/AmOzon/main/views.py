from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'products' : Product.objects.all()})

def cart(request):
    return render(request, 'main/cart.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/details.html' 
    context_object_name = 'product'
