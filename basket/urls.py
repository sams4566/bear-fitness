from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_basket, name='current_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
