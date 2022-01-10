from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_basket, name='current_basket'),
    path('add1/<item_id>/', views.add_to_basket1, name='add_to_basket1'),
    path('add2/<item_id>/', views.add_to_basket2, name='add_to_basket2'),
    path('update/<item_id>/', views.update_basket, name='update_basket'),
    path('delete/<item_id>/', views.delete_basket_item, name='delete_basket_item'),
]
