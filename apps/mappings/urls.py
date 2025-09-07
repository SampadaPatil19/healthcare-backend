from django.urls import path
from .views import MappingListCreateView, PatientMappingView, MappingDeleteView

urlpatterns = [
    path("mappings/", MappingListCreateView.as_view(), name="mapping-list-create"),
    path("mappings/<int:patient_id>/", PatientMappingView.as_view(), name="patient-mappings"),
    path("mappings/delete/<int:pk>/", MappingDeleteView.as_view(), name="mapping-delete"),
]
