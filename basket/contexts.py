from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):
    """
    Stores the basket items and allows the basket to
    be available in all documents
    """
    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for item_id, item_info in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        for size, quantity in item_info['chosen_sizes'].items():
            item_cost = item.cost
            total += item_cost
            placeholder_size = size.upper()
            basket_items.append({
                'item': item,
                'item_id': item_id,
                'size': size,
                'placeholder_size': placeholder_size,
                'quantity': quantity,
            })

    context = {
        'basket_items': basket_items,
        'total': total,
    }
    return context
