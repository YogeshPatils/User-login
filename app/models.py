from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUserModel(User):
    profile_picture=models.ImageField(upload_to='profile_picture/')
    gender=models.CharField(max_length=10,choices=[['male','Male'],['female','Female']])
    