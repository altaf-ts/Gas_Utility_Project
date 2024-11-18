from django.contrib import admin
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep the default admin URL
    path('', views.home, name='home'),  # Add this line to map the root URL to the home view
    path('create/', views.submit_request, name='submit_request'),
    path('status/', views.request_status, name='request_status'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('update/<int:id>/', views.update_status, name='update_status'),
]
