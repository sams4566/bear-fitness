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
            category=category
        )
        self.assertEqual(str(item), 'test_item')


class TestItemForm(TestCase):

    def test_name_must_be_entered(self):
        category = Category.objects.create(name='test_category')
        form = ItemForm({
            'name': '',
            'cost': '50',
            'reviews': '4',
            'category': category
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


class TestItemViews(TestCase):

    def test_retrieve_item_list(self):
        page = self.client.get('/items/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'items/all_items.html')

    def test_retrieve_add_item_html(self):
        page = self.client.get('/items/add/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'items/add_item.html')