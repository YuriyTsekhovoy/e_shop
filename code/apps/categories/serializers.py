from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.categories.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


