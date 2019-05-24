from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.tax.models import Tax


class TaxSerializer(ModelSerializer):

    class Meta:
        model = Tax
        fields = '__all__'
