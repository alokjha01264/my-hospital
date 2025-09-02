from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.age})"
