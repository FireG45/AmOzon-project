from main.models import Product
from userauth.models import Seller, User, Basket
from django.test import TestCase

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
