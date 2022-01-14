from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from checkout.webhook_handler import WebhookHandler

import stripe

@require_POST
@csrf_exempt
def my_webhook_view(request):
    """
    Listens to which webhook is returns from the 
    'WebhookHandler' class in webhook_handler.py. Once 
    a webhook is returned this is displayed in stripe for 
    the stripe user to view.
    """
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
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    handler = WebhookHandler(request)

    event_type = event['type']

    event_route = {
        'payment_intent.succeeded': handler.payment_intent_succeeded,
        'payment_intent.payment_failed': handler.payment_intent_payment_failed
    }

    event_handler = event_route.get(event_type, handler.event_handle)

    result = event_handler(event)
    return result