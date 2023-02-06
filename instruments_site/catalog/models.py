from django.db import models
from decimal import Decimal
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('categorycatalog', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Catalog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    code = models.IntegerField(unique=True, verbose_name='Код')
    vendor_code = models.CharField(max_length=100, verbose_name='Артикул')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    availability = models.CharField(max_length=100, verbose_name='Наличие')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена из парсинга', null=True)
    img_url = models.URLField(verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

    def get_price(self):
        return f'{(self.price * Decimal(1.25)):.{2}f}'

    def get_absolute_url(self):
        return reverse('tovar', kwargs={'pk': self.pk})

    def get_brand_url(self):
        return reverse('brandcatalog', kwargs={'brand_title': self.brand})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


