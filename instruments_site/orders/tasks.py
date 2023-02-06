from .telegram import send_message
from .models import Order, OrderItem
from celery import shared_task
from catalog.models import Catalog


@shared_task
def order_created_send_message(order_id):
    order = Order.objects.get(id=order_id)
    items = OrderItem.objects.filter(order_id=order_id)
    message = 'Новый заказ №{}! \n Имя, фамилия: {} {}' \
              '\n Адрес: {} \n Номер телефона: {} \n' \
              'К ОПЛАТЕ: {}руб. \n --------------- \n'.format(order.id, order.first_name, order.last_name,
                                                              order.addres, order.tel, order.get_total_cost_ship())
    for item in items:
        obj = Catalog.objects.get(id=item.product_id)
        message += 'Наименование: {}\n Код: {}\n Артикул: {}\n Бренд: {}\n' \
                   ' Кол-во: {}\n Цена за ед: {}руб.\n' \
                   ' Итого: {}руб.\n --------------- \n'.format(obj.title, obj.code, obj.vendor_code,
                                                                obj.brand, item.quantity, item.price,
                                                                item.get_cost()
                                                                )
    return send_message(message)
