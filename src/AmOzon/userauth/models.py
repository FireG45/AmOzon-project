from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from main.models import Product
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

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f"Корзина {self.user.username} Продукт {self.product.title}"