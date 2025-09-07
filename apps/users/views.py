from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Register API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Login API using SimpleJWT
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
