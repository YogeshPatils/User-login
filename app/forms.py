from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=['first_name','last_name','username','email','profile_picture','gender']
        