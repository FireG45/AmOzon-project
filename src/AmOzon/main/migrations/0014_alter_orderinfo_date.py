# Generated by Django 4.1.7 on 2023-04-23 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_orderinfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
