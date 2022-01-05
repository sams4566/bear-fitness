from django.test import TestCase
from .models import Item, Category
from .forms import ItemForm
from django.shortcuts import reverse
from urllib.parse import urlencode


class TestItemModel(TestCase):

    def test_item_string_gives_back_item_name(self):
        category = Category.objects.create(name='test_category')
        item = Item.objects.create(
            name='Test Item',
            cost='50',
            reviews='4',
            category=category
        )
        self.assertEqual(str(item), 'Test Item')


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
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/all_items.html')

    def test_retrieve_add_item_html(self):
        response = self.client.get('/items/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/add_item.html')

    def test_retrieve_edit_item_html(self):
        category = Category.objects.create(name='test_category', display_name='Test Category')
        item = Item.objects.create(
            name='Test Item',
            cost='50',
            reviews='4',
            category=category,
        )
        response = self.client.get(f'/items/edit/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/edit_item.html')


    def test_deleting_item(self):
        category = Category.objects.create(name='test_category', display_name='Test Category')
        item = Item.objects.create(
            name='Test Item',
            cost='50',
            reviews='4',
            category=category,
        )
        response = self.client.get(f'/items/delete_item/{item.id}/')
        self.assertRedirects(response, '/items/')
        list_of_items = Item.objects.filter(id=item.id)
        self.assertFalse(list_of_items)

    def test_item_added(self):
        category = Category.objects.create(name='test_category', display_name='Test Category')
        data = urlencode({
            'name': 'Item name edited',
            'cost': '50',
            'reviews': '4',
            'category': category.id,
            'sku': '123',
            'image': 'dumbbell.jpg',
            'bio': 'Test bio',
        })
        response = self.client.post('/items/add/', data, content_type="application/x-www-form-urlencoded")
        self.assertRedirects(response, '/items/1/')

    def test_edited_item(self):
        category = Category.objects.create(name='test_category', display_name='Test Category')
        item = Item.objects.create(
            name='Test Item',
            cost='50',
            reviews='4',
            category=category,
            sku='123',
            image='/media/dumbbell.jpg',
            bio='Test bio',
        )
        data = urlencode({
            'name': 'Item name edited',
            'cost': '50',
            'reviews': '4',
            'category': category.id,
            'sku': '123',
            'image': 'dumbbell.jpg',
            'bio': 'Test bio',
        })
        response = self.client.post(f'/items/edit/{item.id}/', data, content_type="application/x-www-form-urlencoded")
        self.assertRedirects(response, f'/items/{item.id}/')
        edited_item = Item.objects.get(id=item.id)
        self.assertEqual(edited_item.name, 'Item name edited')

    def test_deleting_item(self):
        category = Category.objects.create(name='test_category', display_name='Test Category')
        item = Item.objects.create(
            name='Test Item',
            cost='50',
            reviews='4',
            category=category,
        )
        response = self.client.get(f'/items/delete_item/{item.id}/')
        self.assertRedirects(response, '/items/')
        list_of_items = Item.objects.filter(id=item.id)
        self.assertFalse(list_of_items)
