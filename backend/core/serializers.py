from rest_framework import serializers
from .models import CanvassList, Item, MasterProduct

class CanvassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvassList
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MasterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProduct
        fields = '__all__'
