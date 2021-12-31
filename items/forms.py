from .models import Item
from django import forms


class AddItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('category', 'name', 'bio',
                  'sku', 'cost', 'reviews',
                  'image',)
