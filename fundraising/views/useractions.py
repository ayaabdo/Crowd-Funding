from django.shortcuts import render, get_object_or_404, redirect
from fundraising.models.project import Project
from fundraising.models.user_donation import Donation
from fundraising.models.report_project import ReportAProject

def makeDonation(request, project_id):
    project = Project.objects.get(id=project_id)
    project.total_donation += request.POST['donation']
    project.save()
    donation = Donation.objects.create(user_ID=request.user, project_ID=project,
                                       amount_of_donation=request.POST['donation'])
    return redirect('view_project')

def reportAproject(request, project_id):
    project = Project.objects.get(id=project_id)
    ReportAProject.objects.create(user_ID=request.user, project_ID=project,
                                           description=request.POST.get('report-content'))
    return redirect('project_list')

def rate(request, project_id):
    pass

def reportAcomment(request, project_id, comment_id):
    pass

def comment(request, project_id):
    pass