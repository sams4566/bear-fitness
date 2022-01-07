from .models import Item, Review
from django import forms


class ItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('category', 'name', 'bio',
                  'sku', 'cost', 'image',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)