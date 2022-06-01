from django.shortcuts import render
from rest_framework import generics

from .serializers import ItemSerializer, CartSerializer, LikeSerializer
from .models import Item, LikeProduct, CartProduct


def index(request):
    return render(request, 'index.html')
 
 
class ItemAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CartAPIView(generics.ListAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer


class LikeAPIView(generics.ListAPIView):
    queryset = LikeProduct.objects.all()
    serializer_class = LikeSerializer


class LikeDestroyView(generics.DestroyAPIView):
    queryset = LikeProduct.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'item'


class LikeCreatetView(generics.ListCreateAPIView):
    queryset = LikeProduct.objects.all()
    serializer_class = LikeSerializer


class RemoveFromCartView(generics.DestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'item'


class AddToCartView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer
