from django.urls import path
from django.conf.urls import url
from .views import projects, home

urlpatterns = [
    path('home', home.index, name='home'),
    path('item', projects.index, name='item_list'),
    url(r'^item/(?P<item_id>\d+)/$', item.read, name='item_read'),
    path('item/add', projects.create, name='item_add'),

]