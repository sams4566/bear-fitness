from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('<int:item_id>/', views.item_info, name='item_info'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<item_id>/', views.delete_item, name='delete_item'),
    path('delete_review/<review_id>/', views.delete_review, name='delete_review'),
]
