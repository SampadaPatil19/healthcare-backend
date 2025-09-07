from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer
from .models import Doctor
from .serializers import DoctorSerializer


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only patients of the logged-in user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Assign the logged-in user as owner
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own patients
        return Patient.objects.filter(user=self.request.user)
    
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # only authenticated users can POST

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # require authentication for all operations
