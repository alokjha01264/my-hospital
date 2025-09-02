from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse

# Define a simple view function for the homepage
def home(request):
    return HttpResponse("<h1>API Server is Running</h1><p>Welcome to the myHospital Backend API.</p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),       # For the auth endpoints
    path('api/patients/', include('patients.urls')),   # for patient endpoints
    path('api/doctors/', include('doctors.urls')),     # for doctor endpoints 
    path('api/mappings/', include('mappings.urls')),   # for patient to doctor mapping endpoints
]
