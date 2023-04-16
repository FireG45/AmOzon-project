from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from userauth.models import Basket, User
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'products' : Product.objects.all()})

@login_required
def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(b.price() for b in baskets)
    context = {
        'baskets' : baskets,
        'total_sum' : total_sum,
    }
    return render(request, 'main/cart.html', context)

@login_required
def checkout(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(b.price() for b in baskets)
    context = {
        'baskets' : baskets,
        'total_sum' : total_sum,
        'total_count' : baskets.count()
    }
    return render(request,'main/chekout.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/details.html' 
    context_object_name = 'product'

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def remove_from_cart(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def end_checkout(request):
    for b in Basket.objects.filter(user=request.user):
        b.delete()
    return HttpResponseRedirect('/')
