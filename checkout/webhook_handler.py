from django.http import HttpResponse

class WebhookHandler:

    def __init__(self, request):
        self.request = request

    def event_handle(self, event):
        return HttpResponse(
            content='Unhandled event type: {}'.format(event.type),
            status=200)

    def payment_intent_succeeded(self, event):
        intent = event.data.object
        payment_id = intent.id
        basket = intent.metadata.basket

        return HttpResponse(
            content=f'PaymentIntent was successful: {event["type"]}',
            status=200)

    def payment_intent_intent_failed(self, event):
        return HttpResponse(
            content='Payment failed: {}'.format(event.type),
            status=200)