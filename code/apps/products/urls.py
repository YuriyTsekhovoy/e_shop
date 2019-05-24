from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.products.views import (ProductAPIViewSet,
                                 ProductAttributeAPIViewSet, ProductCategoryAPIViewSet,
                                 ReviewAPIViewSet)

urlpatterns = []

router = DefaultRouter()
router.register(r'products', ProductAPIViewSet,
                base_name='api-products')
urlpatterns += router.urls
