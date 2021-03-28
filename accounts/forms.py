from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('mobile_number', 'birth_date','face_profile','country')

