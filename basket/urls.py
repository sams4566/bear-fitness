from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_basket, name='current_basket'),
]
