from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .models import SKU
from .search_indexes import SKUIndex


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ('id', 'name', 'price', 'default_image_url', 'comments')


class SKUIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes = [SKUIndex]
        fields = ('text', 'id', 'name', 'price', 'default_image_url', 'comments')