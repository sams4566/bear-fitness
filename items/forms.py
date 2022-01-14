from .models import Item, Review
from django import forms


class ItemForm(forms.ModelForm):
    """
    Form that allows superusers to add new items to the site
    """
    class Meta:
        model = Item
        fields = ('category', 'name', 'bio',
                  'sku', 'cost', 'image',)


class ReviewForm(forms.ModelForm):
    """
    Form that allows users to add reviews to an item
    """
    class Meta:
        model = Review
        fields = ('body',)
