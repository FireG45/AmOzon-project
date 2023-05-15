# Generated by Django 4.1.7 on 2023-05-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_orderinfo_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='speed',
            field=models.SmallIntegerField(default=200, verbose_name='Тип отправления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(default='Передан продавцу', max_length=50),
        ),
    ]
