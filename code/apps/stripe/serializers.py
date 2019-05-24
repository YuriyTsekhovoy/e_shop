from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.attributes.models import Attribute, AttributeValue


class AttributeSerializer(ModelSerializer):

    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeValueSerializer(ModelSerializer):

    class Meta:
        model = AttributeValue
        fields = '__all__'
