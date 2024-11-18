from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm, UpdateStatusForm
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    return render(request, 'customer_service/home.html')

# Submit a new service request
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

# View all the requests of a user
@login_required
def request_status(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/request_status.html', {'requests': requests})

# Manage service requests (Admin/Employee)
@login_required
def manage_requests(request):
    search_query = request.GET.get('search', '')
    if search_query:
        requests = ServiceRequest.objects.filter(id__icontains=search_query)
    else:
        requests = ServiceRequest.objects.all()
    return render(request, 'customer_service/manage_requests.html', {'requests': requests})

# Update status of service request
@login_required
def update_status(request, id):
    request_to_update = get_object_or_404(ServiceRequest, id=id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=request_to_update)
        if form.is_valid():
            form.save()
            return redirect('manage_requests')
    else:
        form = UpdateStatusForm(instance=request_to_update)
    return render(request, 'customer_service/update_status.html', {'form': form, 'request': request_to_update})
