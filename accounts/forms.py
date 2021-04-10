from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
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
    image_path = forms.ImageField(required=True, label=_("change photo"),
                                  widget=forms.FileInput({
                                      'class': 'custom-file-input text-info',
                                      'placeholder': 'file path'}))


    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number',
                  'email', 'password1', 'password2', 'image_path')



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
    country = forms.RegexField(
                                regex=r'^[a-zA-Z]{2,}$',
                                max_length=50,
                                required=False,
                                widget=forms.TextInput({    
                                   'class': 'form-control form-control-user',
                                   'id': 'country',
                                   'placeholder': 'country'}))

    image_path = forms.ImageField(
                                widget=forms.FileInput(attrs={
                                    'class': 'custom-file-input'}), 
                                required=False)
                                                                                                                 
    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number',
                   'image_path', 'birth_date', 'face_profile', 'country')




class PasswordResetForm(PasswordResetForm):
    """PasswordResetForm form which uses boostrap CSS."""
    email = forms.EmailField(label=_("Email"), max_length=254,
                             widget=forms.TextInput({
                                 'class': 'form-control form-control-user',
                                 'placeholder': 'E-mail'}))


class SetPasswordForm(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'password_notvalid': _("Password must of 8 Character which contain"
                               + "alphanumeric with at least 1 special character and 1 uppercase."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput({'class': 'form-control form-control-user',
                                    'placeholder': 'New password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput({'class': 'form-control form-control-user',
                                    'placeholder': 'New password confirmation'}),
    )

