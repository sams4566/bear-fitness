from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'full_name', 'email', 'telephone', 'address_line1',
                  'address_line2', 'city', 'county', 'country', 'postcode',)