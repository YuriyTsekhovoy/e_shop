from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer