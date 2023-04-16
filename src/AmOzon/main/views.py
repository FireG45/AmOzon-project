from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Product
from userauth.models import Basket, Seller
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CreateProduct

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'products' : Product.objects.all()})

@login_required(login_url='/userauth/login')
def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(b.price() for b in baskets)
    context = {
        'baskets' : baskets,
        'total_sum' : total_sum,
    }
    return render(request, 'main/cart.html', context)

@login_required(login_url='/userauth/login')
def checkout(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(b.price() for b in baskets)
    context = {
        'baskets' : baskets,
        'total_sum' : total_sum,
        'total_count' : baskets.count()
    }
    return render(request,'main/chekout.html', context)

@permission_required('main.', login_url='userauth/seller_login/')
def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = Seller.objects.get(id=request.user.id)
            product.save()
            return redirect('seller_profile')
        else:
            error = form.errors

    form = CreateProduct()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "main/create.html", data)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/details.html' 
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/update.html' 
    context_object_name = 'product'
    success_url = '/seller_profile'
    
    form_class = CreateProduct

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/delete.html' 
    context_object_name = 'product'
    success_url = '/seller_profile'


@login_required(login_url='/userauth/login')
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

@login_required(login_url='/userauth/login')
def remove_from_cart(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='/userauth/login')
def end_checkout(request):
    for b in Basket.objects.filter(user=request.user):
        b.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/userauth/login')
def user_profile(request):
    return HttpResponseRedirect('/')

@permission_required('main.', login_url='userauth/seller_login/')
def seller_profile(request):
    seller = Seller.objects.get(id=request.user.id)
    products = Product.objects.filter(seller=seller)
    data = {
        'products' : products,
    }
    return render(request, "main/seller_profile.html", data)

