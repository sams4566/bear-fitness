from django.shortcuts import render
from .forms import OrderForm
from django.conf import settings
from basket.contexts import basket_contents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe.api_key = stripe_secret_key
    currency = settings.STRIPE_CURRENCY
    present_basket = basket_contents(request)
    total_cost = present_basket['total']
    stripe_total = round(total_cost * 100)
    intent = stripe.PaymentIntent.create(
        currency=currency,
        amount=stripe_total, 
    )
    print(intent)

    basket = request.session.get('basket', {})
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
