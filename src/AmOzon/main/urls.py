"""AmOzon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('userauth/', include("userauth.urls")),
    path('<int:pk>', views.ProductDetailView.as_view(), name="details"),
    path('baskets/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('baskets/remove/<int:basket_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout',views.checkout, name='checkout'),
    path('end_checkout',views.end_checkout, name='end_checkout'),
    path('cart', views.cart, name='cart'),
    path('tovar',views.tovar),
    path('change',views.change),
    path('delete',views.delete)
]
