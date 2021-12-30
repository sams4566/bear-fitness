from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('<int:item_id>/', views.item_info, name='item_info'),
    path('add/', views.add_item, name='add_item'),
]
