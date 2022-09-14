import requests
import stripe

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


from .models import Item
from .serializer import ItemSerializer

stripe.api_key = 'sk_test_51LhXWLAH1MlYWwwsLCU5zqtPe5jjGlXcS65BccGaxRP' \
                 'v0xPoF22QHYbqVRddBVBF9YAbk4JzAuDECIVY8KdlmjQk00DQIU90nN'


def create_checkout_session(name, price):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': name,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    return session


class ItemViews(GenericViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def list(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            items = self.queryset.objects.filter(id=pk)
            content = {'serializer': self.serializer_class, 'items': items}
            return Response(content)
        return Response({'data': "Метод не разрешен"})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data_request = requests.get(f'http://127.0.0.1:8000/api/buy/{pk}').json()
        name = data_request['name']
        price = data_request['price']
        session = create_checkout_session(name, price)
        return Response({'data': session.id})


class BuyViews(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            item = self.queryset.objects.filter(id=pk)
            # Возвращать session_id
            return item
        return Response({'data': "метод не разрешен"})
