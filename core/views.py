import requests
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


from .models import Item
from .serializer import ItemSerializer


class ItemViews(viewsets.ViewSet):
    queryset = Item
    serializer_class = ItemSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def list(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if request.method == 'GET':
            if pk:
                items = self.queryset.objects.filter(id=pk)
                content = {'serializer': self.serializer_class, 'items': items}
                return Response(content)
            items = self.queryset.objects.all()
            content = {'serializer': self.serializer_class, 'items': items}
            return Response(content)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if request.method == 'POST' and pk:
            data_request = requests.get(f'http://127.0.0.1:8000/api/buy/{pk}').json()
            return Response({'data': data_request})


class BuyViews(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            item = Item.objects.filter(id=pk)
            return item
        items = Item.objects.all()
        return items
