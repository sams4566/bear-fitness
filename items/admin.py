from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'sku', 'cost', 'image',)