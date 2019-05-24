from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.shipping.models import Shipping, ShippingRegion


class ShippingSerializer(ModelSerializer):

    class Meta:
        model = Shipping
        fields = '__all__'


class ShippingRegionSerializer(ModelSerializer):

    class Meta:
        model = ShippingRegion
        fields = '__all__'
