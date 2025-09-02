from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    # just a little upgrade to the app: to show who created the patient
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'contact_number', 'created_by']
