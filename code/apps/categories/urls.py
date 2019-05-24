from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.categories.views import (CategoryAPIViewSet,
                                 )

urlpatterns = []

router = DefaultRouter()
router.register(r'categories', CategoryAPIViewSet,
                base_name='api-categories')
urlpatterns += router.urls

