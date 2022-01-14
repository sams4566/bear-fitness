from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    """
    Allows the details of individual order items to 
    be displayed in the admin
    """
    model = OrderItem
    readonly_fields = ('item_cost',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Allows the order details to be easily modified and displayed 
    for the admin
    """
    list_display = ('order_number', 'order_cost', 
                    'customer_name', 'full_name', 'date',)

    fields = ('order_number', 'stripe_payment_id', 'customer_name', 
              'full_name', 'date', 'order_cost', 'email', 'telephone', 
              'address_line1', 'address_line2', 'city', 'county', 
              'country', 'postcode',)

    readonly_fields = ('order_number', 'date', 'order_cost', 'stripe_payment_id',)

    inlines = (OrderItemAdmin,)
