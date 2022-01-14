from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from items.models import Item
from django.contrib.auth.models import User
import uuid


class Order(models.Model):
    """
    Model that has all of the key information necessary
    to make sure an order is specific to a user
    """
    order_number = models.CharField(max_length=40, editable=False,
                                    null=False)
    stripe_payment_id = models.CharField(max_length=250, default='',
                                         blank=False, null=False)
    customer_name = models.ForeignKey(User, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    order_cost = models.DecimalField(max_digits=15, decimal_places=2,
                                     default=0, null=False)
    email = models.EmailField(max_length=250, blank=False, null=False)
    telephone = models.CharField(max_length=18, blank=False, null=False)
    address_line1 = models.CharField(max_length=100, blank=False, null=False)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(blank=False, null=False, blank_label='Country *')
    postcode = models.CharField(max_length=15, blank=True, null=True)

    def adjust_total(self):
        """
        Updates the order total when an item is added
        """
        self.order_cost = self.orderitems.aggregate(
            Sum('item_cost'))['item_cost__sum'] or 0
        self.save()

    def _create_order_number(self):
        """
        Creates a random order number that is unique
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Everytime an order is saved an order number is
        automatically generated if it isn't already
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    """
    A model that saves the individual items details to the 'Order' model
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False,
                             null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False,
                              null=False, related_name='orderitems')
    item_size = models.CharField(max_length=3, null=False, blank=False)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                    editable=False, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        """
        Returns a generic statement when the model is called
        """
        return f'Order Number: {self.order.order_number} SKU: {self.item.sku}'

    def save(self, *args, **kwargs):
        """
        Automatically saves each items cost when it is added to the model
        """
        self.item_cost = self.item.cost
        super().save(*args, **kwargs)
