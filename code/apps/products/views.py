from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.products.models import (
    Product, ProductAttribute, ProductCategory, Review)
from apps.products.serializers import (
    ProductSerializer, ProductAttributeSerializer,
    ReviewSerializer, ProductCategorySerializer)


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAttributeAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductCategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ReviewAPIViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
