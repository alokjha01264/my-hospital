from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),       # For the auth endpoints
    path('api/patients/', include('patients.urls')),   # for patient endpoints
    path('api/doctors/', include('doctors.urls')),     # for doctor endpoints 
    path('api/mappings/', include('mappings.urls')),   # for patient to doctor mapping endpoints
]
