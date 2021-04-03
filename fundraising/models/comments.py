from django.db import models
from .project import Project
from accounts.models import MyUser

class Comment(models.Model):
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=255)