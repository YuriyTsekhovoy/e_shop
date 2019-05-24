from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.shoppingcart.views import (ShoppingCartAPIViewSet,
                                 )

urlpatterns = []

router = DefaultRouter()
router.register(r'shoppingcart', ShoppingCartAPIViewSet,
                base_name='api-shoppingcart')
urlpatterns += router.urls

