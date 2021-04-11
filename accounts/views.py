from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from .forms import LoginForm, SignupForm, EditProfileForm
from django.contrib.auth.forms import PasswordResetForm
from . import models
from fundraising.models.project import Project
from fundraising.models.categories import Category
from fundraising.models.images import Image
from fundraising.models.user_donation import Donation
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from .tokens import account_activation_token


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form_class = self.form_class
        categories = Category.objects.all()
        return render(request, self.template_name, {'form': form_class, 'categories': categories})


def profile(request, u_id):
    user_data = models.MyUser.objects.get(id=u_id)
    categories = Category.objects.all()
    return render(request, 'accounts/profile.html', {'user_data': user_data, 'categories': categories})


def projects(request, u_id):
    user_projects = Project.objects.filter(user_ID=u_id)
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request, 'accounts/projects.html',
                  {'user_projects': user_projects, 'all_images': images, 'categories': categories})


def donations(request, u_id):
    user_donations = Donation.objects.filter(user_ID=u_id)
    images = Image.objects.all()
    projects = Project.objects.filter(user_ID=u_id)
    categories = Category.objects.all()
    return render(request, 'accounts/donations.html',
                  {'user_donations': user_donations, 'all_images': images, 'projects': projects,
                   'categories': categories})


User = get_user_model()


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'accounts/user_confirm_delete.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print(message)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'accounts/activation_done.html')
    else:
        return HttpResponse('Activation link is invalid!')


# @login_required
def edit_profile(request, u_id):
    categories = Category.objects.all()
    user_data = models.MyUser.objects.get(id=u_id)
    categories = Category.objects.all()
    args = {}
    args['categories'] = categories
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():

            if len(request.FILES) != 0:
                prof_img = request.FILES['image_path']
                fs = FileSystemStorage()
                filename = fs.save(prof_img.name, prof_img)
                uploaded_file_url = fs.url(filename)
            else:
                uploaded_file_url = user_data.image_path

            user_form = form.save()
            user_form.image_path = uploaded_file_url

            user_form.save()
            return redirect('profile', u_id)
        else:
            args['form'] = form
            args['user_data'] = user_data
            return render(request, 'accounts/edit_profile.html', args)
    else:
        form = EditProfileForm(instance=user_data)
        args['form'] = form
        args['user_data'] = user_data
    return render(request, 'accounts/edit_profile.html', args)


def change_password(request, u_id):
    categories = Category.objects.all()
    args = {}
    args['categories'] = categories
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        args['form'] = form
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile', u_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        args['form'] = form
    return render(request, 'accounts/change_password.html', args)
