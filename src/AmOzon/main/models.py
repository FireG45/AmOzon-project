from django.db import models
from userauth.models import User, Basket

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name="Наименование товара", max_length=250)
    description = models.TextField(verbose_name="Описание товара")
    parameters = models.TextField(verbose_name="Дополнительная информация")
    price = models.PositiveBigIntegerField(verbose_name="Цена товара")
    category = models.CharField(verbose_name="Категория товара", max_length=250)
    image = models.URLField(verbose_name="Ссылка на изображение товара")
    seller = models.ForeignKey("userauth.Seller", on_delete=models.CASCADE)

class OrderInfo(models.Model):
    user = models.ForeignKey('userauth.User', on_delete=models.CASCADE)
    seller = models.ForeignKey('userauth.Seller', on_delete=models.CASCADE, related_name='Seller')
    first_name = models.CharField(verbose_name="Имя", max_length=250)
    last_name = models.CharField(verbose_name="Фамилия", max_length=250)
    email = models.EmailField(verbose_name="Электронная почта")
    adress = models.CharField(verbose_name="Адрес", max_length=250)
    post_index = models.SmallIntegerField(verbose_name="Почтовый Индекс")

class OrderItem(models.Model):
    order = models.ForeignKey('main.OrderInfo', on_delete=models.CASCADE)
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE)
