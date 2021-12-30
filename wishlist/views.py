from django.shortcuts import render
from wishlist.models import Wishlist
from django.contrib.auth.models import User
from items.models import Item
from django.shortcuts import get_object_or_404, redirect


def wishlist(request, user_id):
    print(user_id)
    wishlist_items = Wishlist.objects.all().filter(customer_name_id=user_id)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)

 
def add_to_wishlist(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        wishlist_form = Wishlist()
        wishlist_form.size = request.POST['item_size']
        wishlist_form.item = item
        wishlist_form.customer_name = request.user
        wishlist_form.quantity = 1
        wishlist_form.item_cost = item.cost
        wishlist_form.save()
        user_id = request.user.id
        return redirect('wishlist', user_id=user_id)


def delete_wishlist_item(request, wishlist_item_id):
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_item_id)
    user_id = wishlist_item.customer_name.id
    wishlist_item.delete()
    return redirect('wishlist', user_id=user_id)
