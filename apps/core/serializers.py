from rest_framework import serializers
from .models import Patient
from .models import Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')  # user set automatically

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"