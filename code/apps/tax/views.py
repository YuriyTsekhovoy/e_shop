from django.shortcuts import render
from rest_framework import generics, viewsets, filters

from apps.tax.models import Tax
from apps.tax.serializers import TaxSerializer


class TaxAPIViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
