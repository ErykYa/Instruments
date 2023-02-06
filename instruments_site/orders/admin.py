from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'tel', 'addres', 'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInLine]


admin.site.register(Order, OrderAdmin)
