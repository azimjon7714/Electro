# Generated by Django 2.2.7 on 2019-12-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro_shop', '0002_brand_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Товар участвует в акции'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_percent',
            field=models.IntegerField(blank=True, null=True, verbose_name='Процент скидки'),
        ),
    ]
