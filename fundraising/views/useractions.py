from django.shortcuts import render, get_object_or_404, redirect
from fundraising.models.project import Project
from fundraising.models.user_donation import Donation
from fundraising.models.report_project import ReportAProject
from fundraising.models.report_comment import ReportAComment
from fundraising.models.images import Image
from fundraising.models.comments import Comment
from fundraising.models.reply import Reply

from fundraising.models.rate import Rate
from django.http import HttpResponse, JsonResponse
from fundraising.forms.CommentForm import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def makeDonation(request, project_id):
    project = Project.objects.get(id=project_id)
    project.total_donation += int(request.POST.get('donation'))
    project.save()
    donation = Donation.objects.create(user_ID=request.user, project_ID=project,
                                       amount_of_donation=request.POST.get('donation'))
    donation.save()
    return redirect('view_project', project_id)

@login_required
def reportAproject(request, project_id):
    project = Project.objects.get(id=project_id)
    report = ReportAProject.objects.create(user_ID=request.user, project_ID=project,
                                           description=request.POST.get('report-content'))
    report.save()
    return redirect('project_list')

@login_required
def rate(request, project_id):
    template_name = 'projects/view.html'

    SameRecordexit = Rate.objects.filter(user_ID=request.user, proj_ID=project_id).exists()

    if (SameRecordexit == True):
        project = Project.objects.get(id=project_id)
        rate = Rate.objects.get(user_ID=request.user, proj_ID=project)

        old_individual_rate= rate.individual_rate
        old_total_rate=project.total_rate

        rate.individual_rate = request.POST.get('therate')

        new_total_rate=int(old_total_rate) - int(old_individual_rate) + int(request.POST.get('therate'))

        project.total_rate=new_total_rate
        project.overall_avg_rating = new_total_rate / project.number_of_users_rate

        rate.save()
        project.save()
    else:

        project=Project.objects.get(id=project_id)
        rate = Rate.objects.create(user_ID=request.user, proj_ID=project,
                                  individual_rate=request.POST.get('therate'))

        old_total_rate = project.total_rate
        new_total_rate = old_total_rate + int(request.POST.get('therate'))
        project.total_rate = new_total_rate


        old_num_of_users=project.number_of_users_rate
        new_num_of_users= int(old_num_of_users)+ 1
        project.number_of_users_rate = new_num_of_users
        project.overall_avg_rating = new_total_rate / new_num_of_users

        # print(old_total_rate)
        rate.save()
        project.save()

    return redirect(request.META['HTTP_REFERER'])

@login_required
def reportAcomment(request, project_id, comment_id):
    project = Project.objects.get(id=project_id)
    comment = Comment.objects.get(id = comment_id)
    report = ReportAComment.objects.create(user_ID=request.user, comment_ID=comment,
                                           description=request.POST.get('report-comment'))
    report.save()
    return redirect('view_project', project_id)

@login_required
def comment(request,project_id):
    template_name = 'projects/view.html'
    project = Project.objects.get(id=project_id)
    comment= Comment.objects.create(user_ID=request.user, project_ID=project,
                                       comment=request.POST.get('comment'))
    comment.save()
    return redirect('view_project', project_id)

@login_required
def editComment(request):
        the_comment_id = request.POST.get('commentId')
        the_comment = Comment.objects.get(id=the_comment_id)
        the_comment.comment = request.POST.get('comment')
        the_comment.save()
        return redirect('project_list')


@login_required
def reply(request,project_id,comment_id):
    comment = Comment.objects.get(id=comment_id)
    project = Project.objects.get(id=project_id)
    reply = Reply.objects.create(user_ID=request.user, reply=request.POST.get('reply'),
                                     comment=comment)
    reply.save()
    return redirect('project_list')



def deletecomment(request,project_id, comment_id):

    comment = get_object_or_404(Comment, id=comment_id,project_ID=project_id)
    comment.delete()
    return redirect('project_list')