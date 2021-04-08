from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import MyUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    mobile_number = forms.RegexField(regex=r'^01[0125][0-9]{8}$', help_text='invalid phone number')
    # profile_pic = models.ImageField()

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number', 'email', 'password1', 'password2')
