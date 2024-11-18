from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        exclude = ['request_date']  # Exclude 'request_date' as it's non-editable
        fields = ['customer', 'service_type', 'details', 'status']  # Don't include 'request_date' in fields either

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'resolution_date']
        widgets = {
            'resolution_date': forms.DateInput(attrs={'type': 'date'}),
        }
