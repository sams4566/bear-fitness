from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    Allows the details of wishlist items to 
    be displayed and edited in the admin
    """
    list_display = ('item', 'customer_name', 'size', 
                    'item_cost', 'quantity',)

    fields = ('item', 'customer_name', 'size', 
              'item_cost', 'quantity',)

    readonly_fields = ('item_cost',)

