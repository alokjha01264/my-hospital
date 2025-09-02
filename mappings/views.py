from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

# For Listing all mappings or creating new ones (only for patients owned by logged-in user)
class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # To Only return mappings for patients created by the logged-in user
        return PatientDoctorMapping.objects.filter(patient__created_by=self.request.user)

    def perform_create(self, serializer):
        # This to Ensure the patient belongs to the logged-in user
        if serializer.validated_data['patient'].created_by != self.request.user:
            raise PermissionDenied("You cannot assign a doctor to a patient you don't own.")
        serializer.save()

# For Retrieving mappings for a specific patient (only if patient belongs to user)
class MappingRetrieveView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        # To Only return mappings for this patient if the patient belongs to the user
        return PatientDoctorMapping.objects.filter(
            patient__id=patient_id,
            patient__created_by=self.request.user
        )

# For Deleting a mapping (only if patient belongs to user)
class MappingDestroyView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This is to only allow deletion of mappings where patient belongs to user
        return PatientDoctorMapping.objects.filter(patient__created_by=self.request.user)
