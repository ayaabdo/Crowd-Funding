from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import UserDelete

urlpatterns = [
    url(r'^profile/(?P<u_id>\d+)/$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<u_id>\d+)/$', views.edit_profile, name='edit_profile'),
    path('<int:pk>/delete', UserDelete.as_view(), name='user_confirm_delete'),
    url(r'^projects/(?P<u_id>\d+)/$', views.projects, name='projects'),
    url(r'^donations/(?P<u_id>\d+)/$', views.donations, name='donations'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]
