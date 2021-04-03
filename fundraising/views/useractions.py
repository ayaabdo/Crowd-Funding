from django.shortcuts import render, get_object_or_404, redirect
from fundraising.models.project import Project
from fundraising.models.user_donation import Donation
from fundraising.models.report_project import ReportAProject
from fundraising.models.images import Image
from fundraising.models.comments import Comment
from django.http import HttpResponse
from fundraising.forms.CommentForm import CommentForm


def makeDonation(request, project_id):
    project = Project.objects.get(id=project_id)
    project.total_donation += int(request.POST.get('donation'))
    project.save()
    donation = Donation.objects.create(user_ID=request.user, project_ID=project,
                                       amount_of_donation=request.POST.get('donation'))
    donation.save()
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

def comment(request,project_id):
    template_name = 'projects/view.html'
    project = Project.objects.get(id=project_id)
    comment= Comment.objects.create(user_ID=request.user, project_ID=project,
                                       comment=request.POST.get('comment'))
    comment.save()
    return redirect('project_list')

def editComment(request):
    # if request.method == "GET":
    #
    #     the_comment = get_object_or_404(Comment, id=comment_id)
    #     return render(request, "projects/view.html", {"thecomment": the_comment})
    # else:
        # project = Project.objects.get(id=project_id)
        the_comment_id = request.POST.get('commentId')
        the_comment = Comment.objects.get(id=the_comment_id)
        the_comment.comment = request.POST.get('comment')
        the_comment.save()
        return redirect('project_list')


