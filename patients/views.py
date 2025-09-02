from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

# for liisting & creating patients 
class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # To only return patients created by the logged-in user
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Here we automatically set the user who created this patient
        serializer.save(created_by=self.request.user)

# for retrieving, updating, deleting a specific patient
class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # THis to only allow actions on patients created by this user
        return Patient.objects.filter(created_by=self.request.user)
