from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import Order, OrderItem
from items.models import Item
import time
import json


class WebhookHandler:
    """
    A class that helps stripe work out the outcome
    of the payment
    """

    def __init__(self, request):
        """
        Allows access to attributes of the 'request' from stripe
        """
        self.request = request

    def _user_email_confirmation(self, order):
        """
        Creates and sends a confirmation email when an order is created
        """
        business_email = settings.DEFAULT_FROM_EMAIL
        message = render_to_string(
            'checkout/email_confirmations/message.txt',
            {'order': order, 'business_email': business_email})
        title = render_to_string(
            'checkout/email_confirmations/title.txt',
            {'order': order})
        user_email = order.email
        send_mail(
            title,
            message,
            business_email,
            [user_email],
        )

    def event_handle(self, event):
        """
        Lets the stripe user know what the error is if the
        payment didn't succeed or fail
        """
        return HttpResponse(
            content='Unhandled event type: {}'.format(event.type),
            status=200)

    def payment_intent_intent_failed(self, event):
        """
        Lets the stripe user know if the payment failed
        """
        return HttpResponse(
            content='Payment failed: {}'.format(event.type),
            status=200)

    def payment_intent_succeeded(self, event):
        """
        The function checks if an order has already been
        created from the 'checkout' view. If not, an order is
        created and then lets the the stripe user know if the
        payment was successful and if the order was created
        through the 'checkout' view or in the webhook
        """
        intent = event.data.object
        payment_id = intent.id
        billing_details = intent.charges.data[0].billing_details
        order_total = format(intent.charges.data[0].amount / 100, '.2f')
        basket = intent.metadata.basket
        username = intent.metadata.username
        user = User.objects.get(username=username)

        order_created = False
        try_order = 1
        while try_order < 6:
            try:
                order = Order.objects.get(
                    stripe_payment_id=payment_id,
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    telephone__iexact=billing_details.phone,
                    address_line1__iexact=billing_details.address.line1,
                    address_line2__iexact=billing_details.address.line2,
                    city__iexact=billing_details.address.city,
                    county__iexact=billing_details.address.state,
                    country__iexact=billing_details.address.country,
                )
                order_created = True
                break
            except:
                try_order += 1
                time.sleep(1)
        if order_created:
            self._user_email_confirmation(order)
            return HttpResponse(
                content='Order already created: {}'.format(event.type),
                status=200)
        else:
            order = None
            order = Order.objects.create(
                full_name=billing_details.name,
                email=billing_details.email,
                telephone=billing_details.phone,
                address_line1=billing_details.address.line1,
                address_line2=billing_details.address.line2,
                city=billing_details.address.city,
                county=billing_details.address.state,
                country=billing_details.address.country,
                order_cost=order_total,
                stripe_payment_id=payment_id,
                customer_name=user,
            )
            order.save()
            for item_id, item_info in json.loads(basket).items():
                item = get_object_or_404(Item, pk=item_id)
                for size, quantity in item_info['chosen_sizes'].items():
                    item_cost = item.cost
                    order_item = OrderItem(
                        item=item,
                        item_size=size,
                        quantity=quantity,
                        order=order,
                        item_cost=item_cost,
                    )
                    order_item.save()
            self._user_email_confirmation(order)
            return HttpResponse(
                content='PaymentIntent was successful: {}'.format(event.type),
                status=200)
