from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.products.models import (
    Product, ProductAttribute, ProductCategory, Review)


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAttributeSerializer(ModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = '__all__'
