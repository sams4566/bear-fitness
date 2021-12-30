from django.db import models

class Wishlist(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=3, null=False, blank=False)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2, editable=False, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False, default=0)
    order_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False)
    