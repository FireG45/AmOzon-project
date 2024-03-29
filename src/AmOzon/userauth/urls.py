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
from django.urls import path
from userauth import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('seller_login/', views.seller_login, name="seller_login"),
    path('seller_register/', views.seller_register, name="seller_register"),
    path('logout/', views.logout, name="logout"),
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name="order"),
]
