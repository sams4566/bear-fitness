from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form that allows the user to enter all the necessary details
    to purchase an item
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'telephone', 'address_line1',
                  'address_line2', 'city', 'county', 'country', 'postcode',)
