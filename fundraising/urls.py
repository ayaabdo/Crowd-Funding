from django.urls import path
from django.conf.urls import url
from .views import projects, home

urlpatterns = [
    path('home', home.index, name='home'),
  

]
