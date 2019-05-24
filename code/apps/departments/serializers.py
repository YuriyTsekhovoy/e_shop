from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from apps.departments.models import Department


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'
