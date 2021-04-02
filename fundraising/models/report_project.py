from django.db import models
from .project import Project
from accounts.models import MyUser

class ReportAProject(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
