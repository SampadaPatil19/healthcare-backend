from django.db import models

# Create your models here.
from apps.core.models import Doctor
from apps.core.models import Patient 

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("patient", "doctor")  # prevent duplicate mapping

    def __str__(self):
        return f"{self.patient} ↔ Dr. {self.doctor}"