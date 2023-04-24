from .models import User, Seller, Basket
from main.models import Product
from django.test import TestCase

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
        Seller.objects.create()
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


    