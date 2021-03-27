from django.db import models
from .comments import Comment

class ReportAComment(models.Model):
    comment_ID = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
