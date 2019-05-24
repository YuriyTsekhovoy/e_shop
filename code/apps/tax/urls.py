from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.tax.views import TaxAPIViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'tax', TaxAPIViewSet,
                base_name='api-tax')
urlpatterns += router.urls
