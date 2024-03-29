# Generated by Django 4.1.7 on 2023-04-16 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_alter_seller_options'),
        ('main', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='userauth.seller'),
            preserve_default=False,
        ),
    ]
