from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.customers.models import Customer


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


