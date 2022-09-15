from rest_framework import routers
from .views import ItemViews, BuyViews
from django.urls import path, include

router = routers.DefaultRouter()
router.register('buy', BuyViews, basename='buy')
router.register('item', ItemViews, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]
