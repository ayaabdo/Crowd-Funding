from django.shortcuts import render
from django.http import HttpResponse
from fundraising.models.project import Project
# Create your views here.

def index(request):
    projects = Project.objects.all()

    return render(request, 'home/index.html', {'all_projects': projects})

def about(request):
    #projects = Project.objects.all()

    return render(request, 'layout/about.html')
