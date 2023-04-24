from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class User(AbstractUser):
    phone = PhoneNumberField(blank=True, region="RU")
    birth_date = models.DateField(default=datetime.date.today)
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('N', 'Не указан'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Seller(User):
    verbouse_name='Магазины'
    shop_name = models.CharField(max_length=50, verbose_name='Название магазина')
    org_type = models.CharField(max_length=10, verbose_name='Тип организации')
    inn_code = models.CharField(max_length=13, verbose_name='ИНН')
    store_tags = models.TextField(verbose_name='Категории')

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to='main.Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f"Корзина {self.user.username} Продукт {self.product.title} {self.quantity}"
    
    def price(self):
        return self.product.price * self.quantity