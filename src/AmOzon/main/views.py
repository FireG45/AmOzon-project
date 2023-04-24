from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Product, OrderItem, OrderInfo
from userauth.models import Basket, Seller, User
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CreateProduct, CreateOrderInfo

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
    error = ''
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(b.price() for b in baskets)
    sellers_dict = {}
    for b in baskets:
        sellers_dict[b.product.seller] = []

    for b in baskets:
        sellers_dict[b.product.seller] += [b.product]

    if request.method == 'POST':
        form = CreateOrderInfo(request.POST)
        if form.is_valid():
            order_info = form.save(commit=False)
            print(sellers_dict)
            for s in sellers_dict.keys():
                _order_info = form.save(commit=False)
                _order_info.id = None
                _order_info.user = User.objects.get(id=request.user.id)
                _order_info.seller = Seller.objects.get(id=s.id)
                _order_info.save()
                for p in sellers_dict[s]:
                    item = OrderItem.objects.create(product=Product.objects.get(id=p.id), order = OrderInfo.objects.get(id=order_info.id))
                    item.save()
            return redirect('home')
        else:
            error = form.errors

    form = CreateOrderInfo()
    data = {
        'form': form,
        'error': error,
        'baskets' : baskets,
        'total_sum' : total_sum,
        'total_count' : baskets.count()
    }
    return render(request, "main/chekout.html", data)

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
            error = error.as_text()

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
        return render(request, "userauth/user_profile.html")

@permission_required('main.', login_url='userauth/seller_login/')
def seller_profile(request):
    seller = Seller.objects.get(id=request.user.id)
    products = Product.objects.filter(seller=seller)
    orders = OrderInfo.objects.filter(seller=seller)
    data = {
        'products' : products,
        'orders' : orders,
    }
    return render(request, "userauth/seller_profile.html", data)

