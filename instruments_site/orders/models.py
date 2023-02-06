from django.db import models
from catalog.models import Catalog


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    tel = models.CharField(max_length=20, verbose_name='Номер телефона')
    addres = models.CharField(max_length=150, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_cost_ship(self):
        return sum(item.get_cost() for item in self.items.all()) + 7


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='Заказ', on_delete=models.PROTECT)
    product = models.ForeignKey(Catalog, related_name='order_items', verbose_name='Товар', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, verbose_name='Цена', decimal_places=2)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
