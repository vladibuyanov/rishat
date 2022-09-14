import requests
from django.shortcuts import redirect

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Item
from .serializer import ItemSerializer

from .payment import create_checkout_session


class ItemViews(GenericViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def list(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            item = self.queryset.objects.filter(id=pk)[0]
            if item:
                content = {'serializer': self.serializer_class, 'item': item}
                return Response(content)
            return Response({'data': "Не существует"})
        return Response({'data': "Метод не разрешен"})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        # Для тестов
        # data_request = requests.get(f'https://rishatvb.herokuapp.com/api/buy/{pk}/').json()
        # Прод
        data_request = requests.get(f'http://127.0.0.1:8000/api/buy/{pk}').json()
        if data_request:
            name = data_request['name']
            price = data_request['price']
            session = create_checkout_session(name, price, pk)
            return redirect(session.url, code=303)
        return Response({'data': "Не существует"})


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
