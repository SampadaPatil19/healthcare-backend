from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=150)

#     USERNAME_FIELD = 'email'  # Use email for login
#     REQUIRED_FIELDS = ['username']  # username is still required for AbstractUser

#     def __str__(self):
#         return self.email
