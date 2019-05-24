from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.shipping.views import (ShippingAPIViewSet,
                                 ShippingRegionAPIViewSet, )

urlpatterns = []

router = DefaultRouter()
router.register(r'shipping', ShippingRegionAPIViewSet,
                base_name='api-shipping')
urlpatterns += router.urls

