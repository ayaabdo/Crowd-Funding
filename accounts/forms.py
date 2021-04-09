from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import ugettext_lazy as _

from .models import MyUser
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm):
    """UserCreationForm form which uses boostrap CSS."""
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.',
                                 widget=forms.TextInput({
                                     'class': 'form-control form-control-user',
                                     'id': 'first_name',
                                     'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.',
                                widget=forms.TextInput({
                                    'class': 'form-control form-control-user',
                                    'id': 'last_name',
                                    'placeholder': 'last name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput({
                                 'class': 'form-control form-control-user',
                                 'id': 'email',
                                 'placeholder': 'email'}))
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control form-control-user',
                                   'id': 'username',
                                   'placeholder': 'Username'}))
    mobile_number = forms.RegexField(
        regex=r'^01[0125][0-9]{8}$',
        help_text='invalid phone number',
        widget=forms.TextInput({
            'class': 'form-control form-control-user',
            'id': 'mobile_number',
            'placeholder': 'Mobile'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput({
            'class': 'form-control form-control-user',
            'id': 'password1',
            'placeholder': 'Password'}), )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        widget=forms.PasswordInput({
            'class': 'form-control form-control-user',
            'id': 'password1',
            'placeholder': 'Repeat password'}), )
    # image_path = forms.ImageField(required=True, label=_("change photo"),
    #                               widget=forms.FileInput({
    #                                   'class': 'custom-file-input text-info',
    #                                   'placeholder': 'file path'}))


    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number',
                  'email', 'password1', 'password2')



class EditProfileForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.',
                                 widget=forms.TextInput({
                                     'class': 'form-control form-control-user',
                                     'id': 'first_name',
                                     'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.',
                                widget=forms.TextInput({
                                    'class': 'form-control form-control-user',
                                    'id': 'last_name',
                                    'placeholder': 'last name'}))
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control form-control-user',
                                   'id': 'username',
                                   'placeholder': 'Username'}))
    mobile_number = forms.RegexField(
                                regex=r'^01[0125][0-9]{8}$',
                                help_text='invalid phone number',
                                widget=forms.TextInput({
                                    'class': 'form-control form-control-user',
                                    'id': 'mobile_number',
                                    'placeholder': 'Mobile'}))
    birth_date = forms.CharField(
                               widget=forms.TextInput({
                                   'class': 'form-control form-control-user',
                                   'id': 'birth_date',
                                   'placeholder': 'birth_date',
                                   'type':'date'
                                   }))  
    face_profile = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput({
                                   'class': 'form-control form-control-user',
                                   'id': 'face_profile',
                                   'placeholder': 'face_profile'})) 
    country = forms.CharField(max_length=50,
                               required=False,
                               widget=forms.TextInput({    
                                   'class': 'form-control form-control-user',
                                   'id': 'country',
                                   'placeholder': 'country'}))                                                                                               
    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number',
                   'image_path', 'birth_date', 'face_profile', 'country')      

