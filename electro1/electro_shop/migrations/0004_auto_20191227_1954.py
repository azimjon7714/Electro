# Generated by Django 2.2.7 on 2019-12-27 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electro_shop', '0003_auto_20191217_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название галереи')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testPhoto/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='TestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electro_shop.Gallery', verbose_name='Галерея')),
            ],
            options={
                'verbose_name': 'Тестовый продукт',
                'verbose_name_plural': 'Тестовые продукты',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=models.ManyToManyField(to='electro_shop.Photo', verbose_name='Фотографии'),
        ),
    ]
