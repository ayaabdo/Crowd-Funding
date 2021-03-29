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

def index(request):
    # list all items from database
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'all_projects': projects})

def view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/view.html', {'project_details': project})

def create(request):
    #ImageFormSet = modelformset_factory(Image, form=ImageForm)

    if request.method == "GET":
        '''projectForm = ProjectForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'project/add.html',
                      {'all_projects': projectForm, 'all_project_images': formset})'''
        tags = Tag.objects.all()
        cats = Category.objects.all()
        #projects_images = Image.objects.all()
        return render(request, 'projects/add.html', {'all_categories': cats, 'all_tags': tags})
    else:
        if request.method == "POST":
            # images will be in request.FILES
            #form = ImageForm(request.POST or None, request.FILES or None)
            cat = Category.objects.get(id=request.POST.get('cat_id'))
            project_obj = Project.objects.create(
                title=request.POST.get('title'), details=request.POST.get('details'),
                cat_id=cat, total_target=request.POST.get('target'),
                total_donation=request.POST.get('donation'), created_at=request.POST.get('created_at'),
                start_date=request.POST.get('start_date'), end_date=request.POST.get('end_date'))

            images = request.FILES.getlist('file[]')
            for img in images:
                fs = FileSystemStorage()
                img_path = fs.save(img.name, img)
                images = Image.objects.create(proj_id=project_obj, image=img_path)
                images.save()

            tags = request.POST.getlist('tags_id')
            for elem in tags:
                selected_tag = Tag.objects.get(id=elem)
                project_obj.tags.add(selected_tag)
            project_obj.save()
            return HttpResponse(Image.image_path)
            #return redirect('project_list')

def reportAproject(request, project_id):
    pass

def reportAcomment(request, project_id, comment_id):
    pass

def comment(request, project_id):
    pass