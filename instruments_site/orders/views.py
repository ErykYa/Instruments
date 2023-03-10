from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created_send_message


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            cart.clear()
            order_created_send_message(order.id)
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html', {'cart': cart,
                                                  'form': form})
