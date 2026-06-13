from rest_framework import viewsets
from .models import CanvassList, Item, MasterProduct
from .serializers import CanvassListSerializer, ItemSerializer, MasterProductSerializer

class CanvassListViewSet(viewsets.ModelViewSet):
    queryset = CanvassList.objects.all()
    serializer_class = CanvassListSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MasterProductViewSet(viewsets.ModelViewSet):
    queryset = MasterProduct.objects.all()
    serializer_class = MasterProductSerializer
