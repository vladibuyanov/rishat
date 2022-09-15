import requests
from django.shortcuts import get_object_or_404

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Item
from .serializer import ItemSerializer

from .payment import create_checkout_session


class ItemViews(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def list(self, request, *args, **kwargs):
        return Response({'data': "метод не разрешен"})

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        item = get_object_or_404(self.queryset, id=pk)
        name = item.name
        description = item.description
        price = item.price
        items = {'name': name, 'description': description, 'price': price}
        return Response(items)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        # Продакшн
        # data_request = requests.get(f'https://rishatvb.herokuapp.com/api/buy/{pk}/').json()
        # Для тестов
        session_id = requests.get(f'http://127.0.0.1:8000/api/buy/{pk}').json()
        if session_id:
            return Response({'session_id': session_id})


class BuyViews(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        return Response({'data': "метод не разрешен"})

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = self.get_object()
        name = instance.name
        price = instance.price
        session = create_checkout_session(name, price, pk)
        return Response(session.id)
