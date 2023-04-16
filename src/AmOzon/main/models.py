from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name="Наименование товара", max_length=250)
    description = models.TextField(verbose_name="Описание товара")
    parameters = models.TextField(verbose_name="Дополнительная информация")
    price = models.PositiveBigIntegerField(verbose_name="Цена товара")
    category = models.CharField(verbose_name="Категория товара", max_length=250)
    image = models.URLField(verbose_name="Ссылка на изображение товара")
    seller = models.ForeignKey("userauth.Seller", on_delete=models.CASCADE)