from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'status', 'request_date', 'resolution_date')
    list_filter = ('status', 'service_type', 'request_date')
    search_fields = ('customer__name', 'details')
