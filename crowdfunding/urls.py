"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from accounts import forms
from accounts.views import LoginView, signup

'''from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fundraising.urls')),
    path('users/', include('django.contrib.auth.urls'), name='users'),
    path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    # this for social sign-in
    url('', include('social_django.urls', namespace='social')),
    # Forget Password
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             form_class=forms.PasswordResetForm,
             template_name='accounts/forgot-password.html',
             subject_template_name='accounts/password_reset_subject.txt',
             html_email_template_name='accounts/forgot-password-email.html',
         ),
         name='password_reset_form'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/forgot-password-check-mail.html',
         ),
         name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/forgot-password-reset.html',
             form_class=forms.SetPasswordForm,
         ),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/forgot-password-complete.html',
         ),
         name='password_reset_complete'),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)