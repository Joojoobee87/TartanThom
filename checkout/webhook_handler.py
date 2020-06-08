from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle web hooks from Stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Unhandled webhook events from Stripe """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment intent succeeded webhooks from Stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payment intent payment failed webhooks from Stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )