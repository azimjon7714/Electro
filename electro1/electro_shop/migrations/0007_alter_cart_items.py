# Generated by Django 3.2.2 on 2021-05-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro_shop', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='electro_shop.CartItem', verbose_name='Товары'),
        ),
    ]
