
from django.urls import path , include
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^profile/(?P<u_id>\d+)/$', views.profile, name='profile'), 
]