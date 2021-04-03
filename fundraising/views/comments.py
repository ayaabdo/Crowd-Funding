# from fundraising.models.project import Project
# from fundraising.models.comments import Comment
#
# from fundraising.forms.CommentForm import CommentForm
#
# from django.shortcuts import render, get_object_or_404
#
#
#
# def comments_detail(request,project_id):
#     template_name = 'comments/comment.html'
#     project_ID = Project.objects.get(id=project_id)
#    # // project_ID = get_object_or_404(Project, id=project_id)
#     # project_ID = get_object_or_404(project_ID, slug=slug)
#     comments = project_ID.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             # new_comment.post = Comment
#
#             # Assign the current user to the comment
#             new_comment.user_ID = request.user
#
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': Project,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})