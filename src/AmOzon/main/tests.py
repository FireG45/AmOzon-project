from main.models import Product
from main.views import *
from userauth.models import Seller, User, Basket
from django.test import TestCase, RequestFactory
from django.shortcuts import HttpResponse
from django.http import HttpRequest

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self) -> None:
        Seller.objects.create()
        User.objects.create(username='user')
        Product.objects.create(price=100, seller_id = 1)

    def test_title_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Наименование товара')

    def test_description_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'Описание товара')

    def test_parameters_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('parameters').verbose_name
        self.assertEquals(field_label,'Дополнительная информация')

    def test_price_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'Цена товара')

    def test_category_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label,'Категория товара')

    def test_image_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label,'Ссылка на изображение товара')


class MainViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )
        self.seller = Seller.objects.create(id=1)
        Product.objects.create(price=100, seller_id = 1)
        OrderInfo.objects.create(id=1,user=self.user, seller = self.seller, post_index = 0)
        self.basket = Basket.objects.create(user=self.user, product=Product.objects.get(id=1), quantity=1)
        self.request = self.factory.get("/")
        self.request.user = self.user


    def test_index_view(self):
        res = index(self.request)
        self.assertTrue(isinstance(res, HttpResponse))

    def test_cart_view(self):
        res = cart(self.request)
        self.assertTrue(isinstance(res, HttpResponse))
    
    def test_checkout_view(self):
        res = checkout(self.request)
        self.assertTrue(isinstance(res, HttpResponse))

    def test_checkout_post(self):
        request = self.factory.post("/")
        request.user = self.user
        res = checkout(request)
        self.assertTrue(isinstance(res, HttpResponse))

    def test_create_view(self):
        res = create(self.request)
        self.assertTrue(isinstance(res, HttpResponse))

    def test_add_view(self):
        self.request.META['HTTP_REFERER'] = None
        res = add_to_cart(self.request, 1)
        self.assertTrue(isinstance(res, HttpResponse))
    
    # def test_remove_from_cart_view(self):
    #     res = remove_from_cart(self.request, self.basket)
    #     self.assertTrue(isinstance(res, HttpResponse))

    def test_end_checkout_view(self):
        res = end_checkout(self.request)
        self.assertTrue(isinstance(res, HttpResponse))
    
    def test_user_profile_view(self):
        res = user_profile(self.request)
        self.assertTrue(isinstance(res, HttpResponse))

    def test_seller_profile_view(self):
        res = seller_profile(self.request)
        self.assertTrue(isinstance(res, HttpResponse))