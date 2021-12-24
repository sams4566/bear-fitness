from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderItem
from items.models import Item
import time
import json

class WebhookHandler:

    def __init__(self, request):
        self.request = request

    def event_handle(self, event):
        return HttpResponse(
            content='Unhandled event type: {}'.format(event.type),
            status=200)

    def payment_intent_succeeded(self, event):
        intent = event.data.object
        print(intent)
        payment_id = intent.id
        billing_details = intent.charges.data[0].billing_details

        order_created = False
        try_order = 1
        while try_order < 6:
            try:
                order = Order.objects.get(
                    stripe_payment_id=payment_id,
                    customer_name__iexact=billing_details.name,
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
        if not order_created:
            return HttpResponse(
                content='Order not created: {}'.format(event.type),
                status=200)
        else:
            return HttpResponse(
                content='Order already created: {}'.format(event.type),
                status=200)
        

    def payment_intent_intent_failed(self, event):
        return HttpResponse(
            content='Payment failed: {}'.format(event.type),
            status=200)