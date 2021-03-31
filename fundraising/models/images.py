from django.db import models
from .project import Project

class Image(models.Model):
    proj_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_path = models.FileField(max_length=255)
