# Generated by Django 4.1.7 on 2023-04-23 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_orderinfo_orderitem_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.orderinfo'),
            preserve_default=False,
        ),
    ]
