from django.urls import path
from django.conf.urls import url
from .views import home, projects

urlpatterns = [
    path('home', home.index, name='home'),
    path('about', home.about, name='about'),
    path('project', projects.index, name='project_list'),
    path('project/add', projects.create, name='add_project'),
    url(r'^project/(?P<project_id>\d+)/$', projects.view, name='view_project'),
    url(r'^project/(?P<project_id>\d+)/report$', projects.reportAproject, name='report_project'),
    url(r'^project/(?P<project_id>\d+)/comment$', projects.comment, name='comment_project'),
    url(r'^project/(?P<project_id>\d+)/(?P<comment_id>\d+)/report$', projects.reportAcomment, name='report_comment'),
]