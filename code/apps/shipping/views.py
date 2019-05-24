from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.shipping.models import Shipping, ShippingRegion
from apps.shipping.serializers import (
    ShippingSerializer, ShippingRegionSerializer,
)


class ShippingAPIViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class ShippingRegionAPIViewSet(viewsets.ModelViewSet):
    queryset = ShippingRegion.objects.all()
    serializer_class = ShippingRegionSerializer


