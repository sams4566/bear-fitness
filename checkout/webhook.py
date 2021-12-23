from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import stripe

# Using Django
@require_POST
@csrf_exempt
def my_webhook_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    event = None
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)