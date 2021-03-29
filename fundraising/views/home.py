from django.shortcuts import render
from django.http import HttpResponse
from fundraising.models.project import Project
# Create your views here.

def index(request):
    projects = Project.objects.filter(active=1)

    return render(request, 'home/index.html', {'all_projects': projects})

