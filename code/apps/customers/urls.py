from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.customers.views import (CustomerAPIViewSet,
                                 )

urlpatterns = []

router = DefaultRouter()
router.register(r'customers', CustomerAPIViewSet,
                base_name='api-customers')
urlpatterns += router.urls

