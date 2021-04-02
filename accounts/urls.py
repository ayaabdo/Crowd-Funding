
from django.urls import path , include
from django.conf.urls import url 
from . import views
from .views import UserDelete

urlpatterns = [
    url(r'^profile/(?P<u_id>\d+)/$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<u_id>\d+)/$', views.edit_profile, name='edit_profile'),
    url(r'^projects/(?P<u_id>\d+)/$', views.projects, name='projects'), 
    path('<int:pk>/delete', UserDelete.as_view(), name='user_confirm_delete'),
]