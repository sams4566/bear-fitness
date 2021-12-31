from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import ItemForm


def all_items(request):
    items = Item.objects.all()
    if 'category' in request.GET: 
            category = request.GET['category'].split(',')
            items = items.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)[0]
            context = {
                'items': items,
                'category': category,
            }
            return render(request, 'all_items.html', context)
    else:
        items = list(Item.objects.all())
        def sort_item(item):
            return item.name
        items.sort(key=sort_item)
        all_products_category = 'All Products'

    context = {
        'items': items,
        'all_products_category': all_products_category,
    }
    return render(request, 'all_items.html', context)


def item_info(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    category = item.category
    similar_items = Item.objects.all().filter(category=category)

    context = {
        'item': item,
        'similar_items': similar_items,
    }
    return render(request, 'item_info.html', context)


def add_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            category = item.category
            similar_items = Item.objects.all().filter(category=category)
            context = {
                'item': item,
                'similar_items': similar_items,
            }
            return render(request, 'item_info.html', context)
    context = {
        'form': form,
    }
    return render(request, 'add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            category = item.category
            similar_items = Item.objects.all().filter(category=category)
            context = {
                'item': item,
                'similar_items': similar_items,
            }
            return render(request, 'item_info.html', context)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'edit_item.html', context)


def delete_item(request, item_id):
    product = get_object_or_404(Item, pk=item_id)
    product.delete()
    items = list(Item.objects.all())
    def sort_item(item):
        return item.name
    items.sort(key=sort_item)
    all_products_category = 'All Products'
    context = {
        'items': items,
        'all_products_category': all_products_category,
    }
    return render(request, 'all_items.html', context)