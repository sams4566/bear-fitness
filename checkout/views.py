from django.shortcuts import render
from .forms import OrderForm
from django.conf import settings

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    basket = request.session.get('basket', {})
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
    }
    return render(request, template, context)
