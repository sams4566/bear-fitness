from django.urls import path
from . import views

urlpatterns = [
    path('<user_id>/', views.wishlist, name='wishlist'),
    path('add/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('update/<item_id>/', views.update_wishlist, name='update_wishlist'),
    path('delete/<wishlist_item_id>/', views.delete_wishlist_item,
         name='delete_wishlist_item'),
]
