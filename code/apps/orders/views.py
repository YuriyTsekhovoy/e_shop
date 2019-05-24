from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.orders.models import OrderDetail, Orders, Audit
from apps.orders.serializers import (
    OrderDetailSerializer, OrderSerializer, AuditSerializer)


class OrderDetailAPIViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderAPIViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class AuditAPIViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer 