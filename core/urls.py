from rest_framework import routers
from .views import ItemViews, BuyViews
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'buy', BuyViews, basename='buy')

urlpatterns = [
    path('item/', ItemViews.as_view({'get': 'list'})),
    path('item/<int:pk>/', ItemViews.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
