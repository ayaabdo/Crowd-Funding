from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from .forms import LoginForm
from django.contrib.auth.forms import PasswordResetForm
from . import models
from fundraising.models.project import Project
from fundraising.models.images import Image
from fundraising.models.user_donation import Donation
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    # test="test"
    # response_template = 'accounts/login.html'
    def get(self, request):
        form_class = self.form_class
        return render(request, self.template_name, {'form' : form_class})

def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            # You can use more than one way like this for resetting the password.
            # ...filter(Q(email=data) | Q(username=data))
            # but with this you may need to change the password_reset form as well.
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "admin/accounts/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'Interface',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("accounts/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset_form.html",
                  context={"password_reset_form": password_reset_form})    


def profile(request,u_id):
    user_data = models.MyUser.objects.get(id=u_id)
    return render(request, 'accounts/profile.html', {'user_data': user_data})

def projects(request,u_id):
    user_projects = Project.objects.filter(user_ID=u_id)
    images = Image.objects.all()
    return render(request, 'accounts/projects.html', {'user_projects': user_projects, 'all_images': images})


def donations(request,u_id):
    user_donations = Donation.objects.filter(user_ID=u_id)
    images = Image.objects.all()
    projects = Project.objects.filter(user_ID=u_id)
    return render(request, 'accounts/donations.html', {'user_donations': user_donations, 'all_images': images, 'projects':projects})


User = get_user_model()
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'accounts/user_confirm_delete.html'

def edit_profile(request,u_id):
    
    if request.method == "GET":
        user_data = models.MyUser.objects.get(id=u_id)
        return render(request, 'accounts/edit_profile.html', {'user_data': user_data})

    else:
        user_data = models.MyUser.objects.get(id=u_id)

        if request.FILES['profile_img'] :
            prof_img = request.FILES['profile_img']
            fs = FileSystemStorage()
            filename = fs.save(prof_img.name, prof_img)
            uploaded_file_url = fs.url(filename)
        else:
            uploaded_file_url = user_data.image_path 
  

        models.MyUser.objects.filter(id=u_id).update(first_name= request.POST.get('firstName'), last_name= request.POST.get('lastName') ,
            password=request.POST.get('password') , mobile_number=request.POST.get('phone') , birth_date=request.POST.get('birthdate') ,
            image_path=uploaded_file_url ,face_profile=request.POST.get('face_profile') , country=request.POST.get('country') ),

        return render(request, 'accounts/edit_profile.html')
        

    
