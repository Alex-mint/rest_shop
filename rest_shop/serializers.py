

from rest_framework import serializers
from .models import Item, CartProduct, LikeProduct


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = ['item',]