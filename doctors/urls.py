from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor_detail'),
]
