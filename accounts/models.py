from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    image_path = models.FileField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=11, unique=False)
    birth_date = models.DateField(null=True, blank=True)
    face_profile = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
