from django.db import models
from .project import Project

class ReportAProject(models.Model):
    #user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
