from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from .models import Order, OrderItem

@receiver(post_save, sender=OrderItem)
def refresh_total_on_save(sender, instance, created, **kwargs):
    instance.order.adjust_total()

@receiver(post_delete, sender=OrderItem)
def refresh_total_on_delete(sender, instance, **kwargs):
    instance.order.adjust_total()
