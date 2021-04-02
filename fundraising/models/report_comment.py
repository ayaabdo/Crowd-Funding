from django.db import models
from .comments import Comment
from accounts.models import MyUser

class ReportAComment(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment_ID = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
