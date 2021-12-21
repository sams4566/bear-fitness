from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_cost',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'order_cost', 'customer_name', 'date',)

    fields = ('order_number', 'customer_name', 'date', 'order_cost', 
              'email', 'telephone', 'address_line1', 'address_line2', 
              'city', 'county', 'country', 'postcode',)

    readonly_fields = ('order_number', 'date', 'order_cost',)

    inlines = (OrderItemAdmin,)
