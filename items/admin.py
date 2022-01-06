from django.contrib import admin
from .models import Category, Item, Rating, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'sku', 'cost', 'image',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'id',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_date', 'body',)