from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer

# For Listing & Creating Doctors
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# For Retrieving, Updating, Deleting a specific Doctor
class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
