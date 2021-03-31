from django.db import models
from .project import Project
#from .user import User
class Comment(models.Model):
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    #user_ID = models.ForeignKey(USer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)