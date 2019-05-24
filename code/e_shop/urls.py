from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('apps.departments.urls')),
    path(r'', include('apps.categories.urls')),
    path(r'', include('apps.attributes.urls')),
    path(r'', include('apps.products.urls')),
    path(r'', include('apps.customers.urls')),
    path(r'', include('apps.orders.urls')),
    path(r'', include('apps.shoppingcart.urls')),
    path(r'', include('apps.tax.urls')),
    path(r'', include('apps.shipping.urls')),
    # path(r'stripe/', include('apps.stripe.urls')),

]
