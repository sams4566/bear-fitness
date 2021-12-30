from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse



def current_basket(request):
    return render(request, 'basket.html')


def add_to_basket(request, item_id):

    quantity = 1
    size = request.POST['item_size']
    print('hello')
    print(size)
    print('hello')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if size not in basket[item_id]['chosen_sizes'].keys():
            basket[item_id]['chosen_sizes'][size] = quantity
        else:
            messages.error(request, "That item is already in your basket")
    else:
        basket[item_id] = {'chosen_sizes': {size: quantity}}

    request.session['basket'] = basket
    print(request.session['basket'])

    return render(request, 'all_items.html')


def update_basket(request, item_id):
    quantity = 1
    basket = request.session.get('basket', {})
    current_size = request.POST['size_id']
    size = request.POST.get('item_size')
    
    if size == current_size:
        messages.error(request, "That size is already in your basket")
    else:
        basket[item_id]['chosen_sizes'][size] = quantity
        del basket[item_id]['chosen_sizes'][current_size]
        if not basket[item_id]['chosen_sizes']:
            basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('current_basket'))


def delete_basket_item(request, item_id):
    size = request.POST['size_id']
    basket = request.session.get('basket', {})

    del basket[item_id]['chosen_sizes'][size]
    if not basket[item_id]['chosen_sizes']:
        basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('current_basket'))