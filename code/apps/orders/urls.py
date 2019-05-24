from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.orders.views import (OrderDetailAPIViewSet,
                               OrderAPIViewSet,
                               AuditAPIViewSet, )

urlpatterns = []

router = DefaultRouter()
router.register(r'orders', OrderAPIViewSet,
                base_name='api-orders')
urlpatterns += router.urls
