from django.db import models
from items.models import Item
from django.contrib.auth.models import User

class Wishlist(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=3, null=False, blank=False)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2, editable=False, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False, default=0)
    