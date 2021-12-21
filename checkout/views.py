from django.shortcuts import render
from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket: 
        messages.error(request, "Add items to the basket to proceed")
        return render(request, 'all_items.html')
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
