from django.shortcuts import render
from django.http import HttpResponse
from fundraising.models.project import Project
from fundraising.models.categories import Category
from fundraising.models.rate import Rate
from fundraising.models.images import Image


def index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    # projectRates = Rate.objects.all().values('proj_ID','overall_avg_rating').extra(order_by=['-overall_avg_rating']) [:5]
    # ratedProjects = []
    # for p in projectRates:
    #     ratedProjects.extend(
    #         list(Project.objects.filter(id=p.get('proj_ID'))))
    ratedProjects = Project.objects.extra(order_by=['-overall_avg_rating'])[:5]

    lastFiveProject = Project.objects.extra(order_by=['-created_at'])[:5]
    featured = Project.objects.all().filter(featured='True').extra(order_by=['-created_at'])[:5]
    context = {
        # 'ratedProjects': ratedProjects ,
        'ratedProjects': ratedProjects,
        'featured': featured,
        # 'projects': projects,
        # 'lastFiveProject': lastFiveProject ,
        # 'categories': categories,
        'all_images': images,
               }
    return render(request, 'home/index.html', context)

def about(request):
    #projects = Project.objects.all()

    return render(request, 'layout/about.html')

def projectsCategory(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'category': category,
               'all_images': images,
               'categories': categories
               }
    return render(request, "home/categoryList.html", context)
    # return HttpResponse("hi")


