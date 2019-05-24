from django.shortcuts import render
from rest_framework import generics, viewsets, filters

# Create your views here.
from apps.departments.models import Department
from apps.departments.serializers import DepartmentSerializer


class DepartmentAPIViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer