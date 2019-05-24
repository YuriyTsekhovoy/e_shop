from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.orders.models import OrderDetail, Orders, Audit


class OrderDetailSerializer(ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class AuditSerializer(ModelSerializer):

    class Meta:
        model = Audit
        fields = '__all__'
