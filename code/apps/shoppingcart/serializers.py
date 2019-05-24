from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.shoppingcart.models import ShoppingCart


class ShoppingCartSerializer(ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'
