from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from fundraising.models.project import Project
from fundraising.models.images import Image
from fundraising.models.categories import Category
#from fundraising.forms.imageform import ImageForm
#from fundraising.forms.projectform import ProjectForm
from django.forms import modelformset_factory
from django.contrib import messages
from fundraising.models.tags import Tag
from fundraising.models.report_project import ReportAProject

def index(request):
    # list all items from database
    projects = Project.objects.all()
    images = Image.objects.all()
    return render(request, 'projects/index.html', {'all_projects': projects, 'all_images': images})

def view(request, project_id):
        project = get_object_or_404(Project, id=project_id)
        images = Image.objects.filter(proj_id=project_id)
        return render(request, 'projects/view.html', {'project_details': project, 'project_images': images})

def create(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        cats = Category.objects.all()
        return render(request, 'projects/add.html', {'all_categories': cats, 'all_tags': tags})
    else:
        if request.method == "POST":
            cat = Category.objects.get(id=request.POST.get('cat_id'))
            donation = request.POST['donation'] if 'donation' in request.POST else 0
            project_obj = Project.objects.create(user_ID=request.user,
                title=request.POST.get('title'), details=request.POST.get('details'),
                cat_id=cat, total_target=request.POST.get('target'),
                total_donation=donation, created_at=request.POST.get('created_at'),
                start_date=request.POST.get('start_date'), end_date=request.POST.get('end_date'))

            image = request.FILES.getlist("file[]")
            for img in image:
                fs = FileSystemStorage()
                img_path = fs.save(img.name, img)
                img_url = fs.url(img_path)
                images = Image(proj_id=project_obj, image_path=img_url)
                images.save()

            tags = request.POST.getlist('tags_id')
            for elem in tags:
                selected_tag = Tag.objects.get(id=elem)
                project_obj.tags.add(selected_tag)
            project_obj.save()
            return redirect('project_list')
