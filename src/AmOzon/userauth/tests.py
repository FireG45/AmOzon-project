from django.http import HttpResponse
from .models import User, Seller, Basket
from main.models import Product
from userauth.views import *
from django.test import TestCase, RequestFactory

# Create your tests here.
class SellerTestCase(TestCase):
    def setUp(self) -> None:
        Seller.objects.create()

    def test_shop_name_label(self):
        seller=Seller.objects.get(id=1)
        field_label = seller._meta.get_field('shop_name').verbose_name
        self.assertEquals(field_label,'Название магазина')

    def test_org_type_label(self):
        seller=Seller.objects.get(id=1)
        field_label = seller._meta.get_field('org_type').verbose_name
        self.assertEquals(field_label,'Тип организации')

    def test_inn_code_label(self):
        seller=Seller.objects.get(id=1)
        field_label = seller._meta.get_field('inn_code').verbose_name
        self.assertEquals(field_label,'ИНН')

    def test_store_tags_label(self):
        seller=Seller.objects.get(id=1)
        field_label = seller._meta.get_field('store_tags').verbose_name
        self.assertEquals(field_label,'Категории')

class BasketTestCase(TestCase):
    def setUp(self) -> None:
        Seller.objects.create(id=1)
        User.objects.create(username='user')
        Product.objects.create(price=100, seller_id = 1)
        Basket.objects.create(user=User.objects.get(id=1), product=Product.objects.get(id=1))
    
    def test__str__(self):
        basket = Basket.objects.get(id=1)
        expected_object_name = "Корзина %s Продукт %s %d" % (basket.user.username, basket.product.title, basket.quantity)
        self.assertEquals(expected_object_name, str(basket))

    def test_price(self):
        basket = Basket.objects.get(id=1)
        self.assertEqual(basket.price(), basket.product.price * basket.quantity)

class ViewsTestCase(TestCase):
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
        self.request_post = self.factory.post("/")
        self.request.user = self.user
        self.request_post.user = self.user

    def test_login_view(self):
        res = login(self.request_post)
        res2 = login(self.request)
        self.assertTrue(isinstance(res, HttpResponse) and isinstance(res2, HttpResponse))

    def test_register_view(self):
        res = register(self.request_post)
        res2 = register(self.request)
        self.assertTrue(isinstance(res, HttpResponse) and isinstance(res2, HttpResponse))

    def test_seller_login_view(self):
        res = seller_login(self.request_post)
        res2 = seller_login(self.request)
        self.assertTrue(isinstance(res, HttpResponse) and isinstance(res2, HttpResponse))

    def test_seller_register_login_view(self):
        res = seller_register(self.request_post)
        res2 = seller_register(self.request)
        self.assertTrue(isinstance(res, HttpResponse) and isinstance(res2, HttpResponse))

    # def test_logout_login_view(self):
    #     res = logout(self.request_post)
    #     res2 = logout(self.request)
    #     self.assertTrue(isinstance(res, HttpResponse) and isinstance(res2, HttpResponse))
