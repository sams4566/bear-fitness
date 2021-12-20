from django.shortcuts import get_object_or_404
from items.models import Item

def basket_contents(request):
    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        total = item.cost
        basket_items.append({
            'item': item,
            'item_id': item_id,
            'quantity': quantity,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
    }
    return context