from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.shoppingcart.models import ShoppingCart
from apps.shoppingcart.serializers import ShoppingCartSerializer


class ShoppingCartAPIViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
