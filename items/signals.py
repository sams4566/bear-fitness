from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from .models import Item, Rating


@receiver(post_delete, sender=Rating)
def refresh_rating_total_on_delete(sender, instance, **kwargs):
    """
    Everytime a star rating is deleted from the 'Rating' model the
    rating_total is updated
    """
    instance.item.adjust_rating_total()


@receiver(post_save, sender=Rating)
def refresh_rating_total_on_save(sender, instance, created, **kwargs):
    """
    Everytime a star rating is added to the 'Rating' model the
    rating_total is updated
    """
    instance.item.adjust_rating_total()
