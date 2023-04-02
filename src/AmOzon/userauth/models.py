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