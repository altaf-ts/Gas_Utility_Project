from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Maintenance', 'Maintenance'),
        ('Billing', 'Billing'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    details = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request by {self.customer.name} - {self.service_type}"
