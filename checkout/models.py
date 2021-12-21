from django.db import models
from django.db.models import Sum
from django.conf import settings
from items.models import Item
import uuid

class Order(models.Model):
    order_number = models.CharField(max_length=40, editable=False, null=False)
    customer_name = models.CharField(max_length=55, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    order_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False)
    email = models.EmailField(max_length=250, blank=False, null=False)
    telephone = models.CharField(max_length=18, blank=False, null=False)
    address_line1 = models.CharField(max_length=100, blank=False, null=False)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=False, null=False)
    postcode = models.CharField(max_length=15, blank=False, null=False)

    def adjust_total(self):
        self.order_cost = self.orderitems.aggregate(Sum('item_cost'))['item_cost__sum'] or 0
        self.save()

    def _create_order_number(self):
        return uuid.uuid4().hex.upper()

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False, related_name='orderitems')
    item_size = models.CharField(max_length=3, null=False, blank=False)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2, editable=False, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False, default=0)