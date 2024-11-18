from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin site
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('', include('customer_service.urls')),  # Include the customer_service app URLs
]
