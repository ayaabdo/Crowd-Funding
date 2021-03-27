from django.db import models
from .project import Project

class ReportAProject(models.Model):
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
