from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    slug = models.SlugField(verbose_name='Альтернативное название')

    class Meta:
        verbose_name='Категории'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название бренда')
    slug = models.SlugField(verbose_name='Альтернативное название')

    class Meta:
        verbose_name='Брэнд'
        verbose_name_plural='Брэнд'

    def __str__(self):
        return self.name

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)



class Product(models.Model):
    category = models.ForeignKey(
                        Category,
                        on_delete=models.CASCADE,
                        verbose_name='Категория')
    brand = models.ForeignKey(
                        Brand,
                        on_delete=models.CASCADE,
                        verbose_name='Брэнд')
    name = models.CharField(max_length=200, verbose_name='Название товара')
    slug = models.SlugField(verbose_name='Альтернативное название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    image = models.ImageField(upload_to=image_folder, verbose_name='Фото товара',)
    available = models.BooleanField(default=True, verbose_name='Товар в наличии')
    sale = models.BooleanField(default=False, verbose_name='Товар участвует в акции', blank=True, null=True)
    sale_percent = models.IntegerField(verbose_name='Процент скидки', blank=True, null=True)

    class Meta:
        verbose_name='Товары'
        verbose_name_plural='Товары'

    def __str__(self):
        return "{0}-{1}".format(self.category, self.name)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

class Photo(models.Model):
    name = models.CharField('Название', max_length=30, default='')
    image = models.ImageField('Фото', upload_to='testPhoto/')

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField('Название галереи', max_length=100)
    photos = models.ManyToManyField(Photo, verbose_name='Фотографии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Галерея'
        verbose_name_plural='Галерея'

class TestProduct(models.Model):
    title = models.CharField('Наименование', max_length=100)
    price = models.PositiveIntegerField('Цена', default=0)
    images = models.ForeignKey(
                    Gallery,
                    verbose_name='Галерея',
                    on_delete=models.SET_NULL,
                    blank=True,
                    null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Тестовый продукт'
        verbose_name_plural='Тестовые продукты'
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                            verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество', default=1)
    item_total = models.DecimalField('Цена', decimal_places=2,
                                                max_digits=9,
                                                default=0.00)
    def __str__(self):
        return "Товар {0}".format(self.product.name)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, verbose_name='Товары', blank=True)
    cart_total = models.DecimalField(
                                            'Сумма',
                                            decimal_places=2,
                                            max_digits=9,
                                            default=0.00)
    def __str__(self):
        return str(self.id)
