from wishlist.views import delete_wishlist_item
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, \
    redirect, reverse, HttpResponse


def current_basket(request):
    """
    View for displaying the current items stored in the
    basket_contents function in contexts.py
    """
    return render(request, 'basket.html')


def add_to_basket1(request, item_id):
    """
    Allows the user to add an item from item_info.html
    to the basket. It throws an error if the same item
    with the same size is already in the basket.
    """
    quantity = 1
    size = request.POST['item_size']
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if size not in basket[item_id]['chosen_sizes'].keys():
            basket[item_id]['chosen_sizes'][size] = quantity
        else:
            messages.error(request, "That item is already in your basket")
    else:
        basket[item_id] = {'chosen_sizes': {size: quantity}}

    request.session['basket'] = basket
    return redirect(reverse('current_basket'))


def add_to_basket2(request, item_id):
    """
    Allows the user to move an item from their wishlist
    to the basket. It throws an error if the same item
    with the same size is already in the basket.
    """
    wishlist_item_id = request.POST['wishlist_item_id']
    quantity = 1
    size = request.POST['item_size']
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if size not in basket[item_id]['chosen_sizes'].keys():
            basket[item_id]['chosen_sizes'][size] = quantity
            if wishlist_item_id:
                delete_wishlist_item(request, wishlist_item_id)
        else:
            messages.error(request, "That item is already in your basket")
    else:
        basket[item_id] = {'chosen_sizes': {size: quantity}}
        if wishlist_item_id:
                delete_wishlist_item(request, wishlist_item_id)

    request.session['basket'] = basket
    return redirect(reverse('current_basket'))


def update_basket(request, item_id):
    """
    Lets the user change the size of the item in the basket.
    It throws an error if the same item with the same size
    is already in the basket.
    """
    quantity = 1
    basket = request.session.get('basket', {})
    current_size = request.POST['size_id']
    size = request.POST.get('item_size')

    if item_id in list(basket.keys()):
        if size not in basket[item_id]['chosen_sizes'].keys():
            basket[item_id]['chosen_sizes'][size] = quantity
            del basket[item_id]['chosen_sizes'][current_size]
        else:
            messages.error(request, "That item is already in your basket")

    request.session['basket'] = basket

    return redirect(reverse('current_basket'))


def delete_basket_item(request, item_id):
    """
    The item is deleted from the basket when the user
    clicks the delete button
    """
    size = request.POST['size_id']
    basket = request.session.get('basket', {})

    del basket[item_id]['chosen_sizes'][size]
    if not basket[item_id]['chosen_sizes']:
        basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('current_basket'))
