from django.contrib import admin
from .models import Category, Item, Rating, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays the 'Category' model details for admins
    """
    list_display = ('name', 'display_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Displays the 'Item' model details for admins
    """
    list_display = ('category', 'name', 'sku', 'cost', 'image',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Displays the 'Rating' model details for admins
    """
    list_display = ('user', 'id',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Displays the 'Review' model details for admins
    """
    list_display = ('review_date', 'body',)