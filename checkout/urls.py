from django.urls import path
from . import views
from .webhook import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_confirmation/<order_number>', views.checkout_confirmation, name='checkout_confirmation'),
    path('save_checkout_info/', views.save_checkout_info, name='save_checkout_info'),
    path('orders/<customer_name_id>/', views.orders, name='orders'),
    path('order_summary/<order_number>/', views.order_summary, name='order_summary'),
    path('webhook/', my_webhook_view, name='my_webhook_view'),
]
