from django.urls import path
from . import views
from .webhook import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_confirmation/<order_number>', views.checkout_confirmation, name='checkout_confirmation'),
    path('webhook/', my_webhook_view, name='my_webhook_view'),
]
