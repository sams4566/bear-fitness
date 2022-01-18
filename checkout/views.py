import json
import stripe
from .forms import OrderForm
from django.views.decorators.http import require_POST
from django.conf import settings
from basket.contexts import basket_contents
from items.models import Item
from .models import OrderItem, Order
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render, get_object_or_404, \
    redirect, reverse


@require_POST
def save_checkout_info(request):
    """
    Adds the users details and current basket to the metadata so that the
    'WebhookHandler' class can use the information for creating an order
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payment_id = request.POST.get('client_secret').split('_secret')[0]
    stripe.PaymentIntent.modify(payment_id, metadata={
        'basket': json.dumps(request.session.get('basket', {})),
        'username': request.user,
    })
    return HttpResponse(status=200)


def checkout(request):
    """
    Initally the checkout.html page is displayed listing the
    items in the basket and collecting all of the information
    requried for a successful payment to take place. Once the
    user has clicked 'Complete payment' an order is created
    using the information provided in the 'OrderForm' and basket.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method != 'POST':
        stripe.api_key = stripe_secret_key
        currency = settings.STRIPE_CURRENCY
        present_basket = basket_contents(request)
        total_cost = present_basket['total']
        stripe_total = round(total_cost * 100)
        intent = stripe.PaymentIntent.create(
            currency=currency,
            amount=stripe_total,
        )
        basket = request.session.get('basket', {})
        order_form = OrderForm()

    else:
        basket = request.session.get('basket', {})

        form_info = {
            'full_name': request.POST['full_name'],
            'telephone': request.POST['telephone'],
            'email': request.POST['email'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_info)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_payment_id = payment_id
            order.save()
            order_cost = 0
            for item_id, item_info in basket.items():
                item = get_object_or_404(Item, pk=item_id)
                for size, quantity in item_info['chosen_sizes'].items():
                    item_cost = item.cost
                    order_cost += item_cost
                    order_item = OrderItem(
                        item=item,
                        item_size=size,
                        quantity=quantity,
                        order=order,
                        item_cost=item_cost,
                    )
                    order_item.save()
            order.order_cost = order_cost
            order.save()
            order_number = order.order_number
        return redirect('checkout_confirmation', order_number=order_number)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_confirmation(request, order_number):
    """
    Once the payment has been successful the current basket is
    deleted and the order is saved to the user. The order details
    are then displayed to the user.
    """
    basket = request.session.get('basket', {})
    if basket:
        del request.session['basket']
    order = get_object_or_404(Order, order_number=order_number)
    order.customer_name = request.user
    order.save()
    order_items = order.orderitems.all()

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, template, context)


def orders(request, customer_name_id):
    """
    A list of the users previously purchased orders are
    displayed starting with the most recent first
    """
    user_id = request.user.id
    orders = Order.objects.all().filter(customer_name_id=user_id).order_by(
        '-date')

    template = 'checkout/orders.html'
    context = {
        'orders': orders,
    }
    return render(request, template, context)


def order_summary(request, order_number):
    """ Displays a specific orders details """
    order = Order.objects.all().filter(order_number=order_number)
    order1 = get_object_or_404(Order, order_number=order_number)
    order_items = order1.orderitems.all()
    user_id = request.user.id

    template = 'checkout/order_summary.html'
    context = {
        'order': order,
        'order_items': order_items,
        'user_id': user_id,
    }
    return render(request, template, context)
