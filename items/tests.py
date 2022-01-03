from django.test import TestCase
from .models import Item, Category
from .forms import ItemForm


class TestItemModel(TestCase):

    def test_item_string_gives_back_item_name(self):
        category = Category.objects.create(name='test_category')
        item = Item.objects.create(
            name='test_item',
            cost='50',
            reviews='4',
        )
        self.assertEqual(str(item), 'test_item')

    