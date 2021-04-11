from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from fundraising.models.project import Project
from fundraising.models.images import Image
from fundraising.models.categories import Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Sum
from accounts.models import MyUser
#from fundraising.forms.imageform import ImageForm
#from fundraising.forms.projectform import ProjectForm
from django.forms import modelformset_factory
from django.contrib import messages
from fundraising.models.tags import Tag
from fundraising.models.rate import Rate
from fundraising.models.report_project import ReportAProject

def index(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()

    return render(request, 'projects/index.html', {'all_projects': projects, 'all_images': images,'categories': categories})

@login_required
def view(request, project_id):
        project = get_object_or_404(Project, id=project_id)
        # tagedProjects = Project.objects.all().filter(tag_id=project.tags)
        images = Image.objects.filter(proj_id=project_id)
        ratequery = Rate.objects.filter(user_ID=request.user, proj_ID=project_id)
        comments =project.comments.filter(active=True)
        allimages = Image.objects.all()
        categories = Category.objects.all()
        # tagProjects = Tag.objects.all().values('project', 'tag_name').order_by('-project').distinct()
        # print(tagProjects)
        # print(project)

        # ProjectsIDS =Tag.objects.order_by('project').values('project').distinct()

        # tagProjects = Tag.objects.all().values('project', 'tag_name').extra(order_by=['-project']).distinct()
        # print(tagProjects)
        # tagedProjects = []
        # tagdic = {}
        # for proj in tagProjects:
        #     if proj['project'] not in tagedProjects :
        #          # print( proj['project'] )
        #          tagedProjects.append(proj['project'])
        #
        # print(tagedProjects)
        # dict={}
        tagProjects = Tag.objects.all().values('project','tag_name').extra(order_by=['-tag_name']).distinct()



        if(ratequery.count() > 0):
            rate = Rate.objects.get(user_ID=request.user, proj_ID=project_id)
            return render(request, 'projects/view.html', {'project_details': project, 'project_images': images,
                                                'comments':comments,'rate':rate.individual_rate,'tagProjects':tagProjects
                                                        ,'all_images':allimages,'categories': categories  })
        else:
            return render(request, 'projects/view.html', {'project_details': project, 'project_images': images,
                                                          'comments': comments,'rate':-1,'tagProjects':tagProjects
                                                          ,'all_images':allimages ,'categories': categories })

        comments =project.comments.filter(active=True)




        # return render(request, 'projects/view.html', {'project_details': project, 'project_images': images,
        #                                               'comments':comments})
@login_required
def create(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        cats = Category.objects.all()
        return render(request, 'projects/add.html', {'all_categories': cats, 'all_tags': tags})
    else:
        if request.method == "POST":
            cat = Category.objects.get(id=request.POST.get('cat_id'))
            #donation = request.POST['donation'] if 'donation' in request.POST else 0
            project_obj = Project.objects.create(user_ID=request.user,
                title=request.POST.get('title'), details=request.POST.get('details'),
                cat_id=cat, total_donation=0,total_target=request.POST.get('target'),
                created_at=request.POST.get('created_at'),
                start_date=request.POST.get('start_date'), end_date=request.POST.get('end_date'))

            image = request.FILES.getlist("file[]")
            if image:
                save_images(image, project_obj)

            tags = request.POST.getlist('tags_id')
            if tags:
                save_tags(tags, project_obj)

            project_obj.save()
            return redirect('project_list')

@login_required
def update(request, project_id):
    images = Image.objects.filter(proj_id=project_id)

    if request.method == "GET":
        project = get_object_or_404(Project, id=project_id)
        tags = Tag.objects.all()
        cats = Category.objects.all()
        return render(request, 'projects/update.html', {'selected_project': project, 'project_images': images, 'all_categories': cats, 'all_tags': tags})

    else:
        cat = Category.objects.get(id=request.POST.get('cat_id'))
        project = get_object_or_404(Project, id=project_id)
        project.title = request.POST.get('title')
        project.details = request.POST.get('details')
        project.cat_id = cat
        project.total_target = request.POST.get('target')

        image = request.FILES.getlist("file[]")
        if image:
            images.delete()
            save_images(image, project)

        tags = request.POST.getlist('tags_id')
        if tags:
            project.tags.clear()
            save_tags(tags, project)

        project.save()
        return redirect('view_project', project_id)


def save_images(image, project):
    for img in image:
        fs = FileSystemStorage()
        img_path = fs.save(img.name, img)
        img_url = fs.url(img_path)
        images = Image(proj_id=project, image_path=img_url)
        images.save()

def save_tags(tags, project):
    for elem in tags:
        selected_tag = Tag.objects.get(id=elem)
        project.tags.add(selected_tag)

        #########################################################################################


def search(request):
    q = request.GET.get('searchy')
    if q:
        print('searchBox')
        project = Project.objects.filter(title__icontains=q)
        images = Image.objects.all()
        categories = Category.objects.all()
        # return show(request, project)
        return render(request, "home/srch.html", {'project': project, 'categories': categories,'all_images': images})

# def show(request, id):
#     # project = Project.objects.get(id=id)
#     project = get_object_or_404(Project, id=id)
#     context = {'project':project,
#                }
#     return render(request, "home/srch.html", context)


def delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project_list')