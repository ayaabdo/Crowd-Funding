from django.db import models
from .comments import Comment
from accounts.models import MyUser
from .project import Project

class ReportAComment(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    comment_ID = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
