# Generated by Django 4.1.7 on 2023-03-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('parameters', models.TextField(verbose_name='Дополнительная информация')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена товара')),
                ('category', models.TextField(verbose_name='Категория товара')),
                ('image', models.URLField(verbose_name='Ссылка на изображение товара')),
            ],
        ),
    ]
