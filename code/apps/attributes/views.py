from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.attributes.models import Attribute, AttributeValue
from apps.attributes.serializers import (
    AttributeSerializer, AttributeValueSerializer)


class AttributeAPIViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeValueAPIViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
