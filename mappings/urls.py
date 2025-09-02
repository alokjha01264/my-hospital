from django.urls import path
from .views import MappingListCreateView, MappingRetrieveView, MappingDestroyView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping_list_create'),
    path('<int:patient_id>/', MappingRetrieveView.as_view(), name='mapping_by_patient'),
    path('delete/<int:pk>/', MappingDestroyView.as_view(), name='mapping_delete'),
]
