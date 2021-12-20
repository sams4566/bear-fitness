from django.shortcuts import render, get_object_or_404
from .models import Item


def all_items(request):
    items = Item.objects.all()
    
    context = {
        'items': items,
    }
    return render(request, 'all_items.html', context)


def item_info(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }
    return render(request, 'item_info.html', context)