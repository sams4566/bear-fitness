from django.shortcuts import render
from wishlist.models import Wishlist
from django.contrib.auth.models import User
from items.models import Item
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def wishlist(request, user_id):
    """
    Displays a list of items saved to the users wishlist
    """
    wishlist_items = Wishlist.objects.all().filter(customer_name_id=user_id)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'user_id': user_id,
    }
    return render(request, template, context)

 
def add_to_wishlist(request, item_id):
    """
    Allows the user to add an item from item_info.html
    to their wishlist. It throws an error if the same item 
    with the same size is already in the wishlist.
    """
    user_id = request.user.id
    wishlist_items = list(Wishlist.objects.all().filter(customer_name_id=user_id))
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        wishlist_form = Wishlist()
        for product in wishlist_items:
            item_size = request.POST['item_size']
            product_id = int(product.item.id)
            if product_id == int(item_id):
                if product.size == item_size:
                    messages.add_message(
                        request,
                        messages.INFO, 
                        "That size is already in your wishlist.", 
                    )
                    template = 'wishlist/wishlist.html'
                    context = {
                        'wishlist_items': wishlist_items,
                    }
                    return render(request, template, context)
        wishlist_form.size = request.POST['item_size']
        wishlist_form.item = item
        wishlist_form.customer_name = request.user
        wishlist_form.quantity = 1
        wishlist_form.item_cost = item.cost
        wishlist_form.save()
        user_id = request.user.id
        return redirect('wishlist', user_id=user_id)

def update_wishlist(request, item_id):
    """
    Lets the user change the size of the item in the wishlist. 
    It throws an error if the same item with the same size 
    is already in the wishlist.
    """
    current_size = request.POST['size_id']
    size = request.POST.get('item_size')
    user_id = request.user.id
    wishlist_items = list(Wishlist.objects.all().filter(customer_name_id=user_id))
    item = get_object_or_404(Item, pk=item_id)
    wishlist_form = Wishlist()
    for product in wishlist_items:
        item_size = request.POST['item_size']
        product_id = int(product.item.id)
        if product_id == int(item_id):
            if product.size == item_size:
                messages.add_message(
                    request,
                    messages.INFO, 
                    "That size is already in your wishlist.", 
                )
                template = 'wishlist/wishlist.html'
                context = {
                    'wishlist_items': wishlist_items,
                }
                return render(request, template, context)
            if product.size == current_size:
                product.delete()
    wishlist_form = Wishlist()
    wishlist_form.size = size
    wishlist_form.item = item
    wishlist_form.customer_name = request.user
    wishlist_form.quantity = 1
    wishlist_form.item_cost = item.cost
    wishlist_form.save()
    return redirect('wishlist', user_id=user_id)

def delete_wishlist_item(request, wishlist_item_id):
    """
    The item is deleted from the wishlist when the user
    clicks the delete button
    """
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_item_id)
    user_id = wishlist_item.customer_name.id
    wishlist_item.delete()
    return redirect('wishlist', user_id=user_id)