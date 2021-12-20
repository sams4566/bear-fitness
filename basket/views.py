from django.shortcuts import render, get_object_or_404



def current_basket(request):
    return render(request, 'basket.html')


def add_to_basket(request, item_id):

    quantity = 1
    basket = request.session.get('basket', {})

    basket[item_id] = quantity
    request.session['basket'] = basket
    print(request.session['basket'])

    return render(request, 'all_items.html')