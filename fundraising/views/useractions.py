from django.shortcuts import render, get_object_or_404, redirect
from fundraising.models.project import Project
from fundraising.models.user_donation import Donation
from fundraising.models.report_project import ReportAProject
from fundraising.models.images import Image
from django.http import HttpResponse

def makeDonation(request, project_id):
    project = Project.objects.get(id=project_id)
    project.total_donation += int(request.POST.get('donation'))
    project.save()
    donation = Donation.objects.create(user_ID=request.user, project_ID=project,
                                       amount_of_donation=request.POST.get('donation'))
    donation.save()
    #images = Image.objects.filter(proj_id=project_id)
    #return render(request, 'projects/view.html', {'project_details': project, 'project_images': images})
    return redirect('view_project', project_id)

def reportAproject(request, project_id):
    project = Project.objects.get(id=project_id)
    report = ReportAProject.objects.create(user_ID=request.user, project_ID=project,
                                           description=request.POST.get('report-content'))
    report.save()
    return redirect('project_list')

def rate(request, project_id):
    pass

def reportAcomment(request, project_id, comment_id):
    pass

def comment(request, project_id):
    pass