from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.departments.views import (DepartmentAPIViewSet,
                                 )

urlpatterns = []

router = DefaultRouter()
router.register(r'departments', DepartmentAPIViewSet,
                base_name='api-departments')
urlpatterns += router.urls

