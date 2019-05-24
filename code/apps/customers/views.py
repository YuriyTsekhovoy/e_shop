from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


class CustomerAPIViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer