from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from .models import Order, OrderItem


@receiver(post_delete, sender=OrderItem)
def refresh_total_on_delete(sender, instance, **kwargs):
    """
    Everytime an order item is deleted from the 'OrderItem' model the
    order_total is updated
    """
    instance.order.adjust_total()


@receiver(post_save, sender=OrderItem)
def refresh_total_on_save(sender, instance, created, **kwargs):
    """
    Everytime an order item is added to the 'OrderItem' model the
    order_total is updated
    """
    instance.order.adjust_total()
