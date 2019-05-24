from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.weldings.views import (AttributeAPIViewSet,
                                 )

urlpatterns = []

router = DefaultRouter()
router.register(r'attributes', AttributeAPIViewSet,
                base_name='api-attributes')
urlpatterns += router.urls

