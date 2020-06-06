from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle web hooks from Stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle webhook events from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )
