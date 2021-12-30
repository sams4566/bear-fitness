from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('item', 'customer_name', 'item_size', 
                    'item_cost', 'quantity',)

    fields = ('item', 'customer_name', 'item_size', 
              'item_cost', 'quantity',)

    readonly_fields = ('item_cost',)

