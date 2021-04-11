from django.db import models
from .project import Project
from accounts.models import MyUser
from .comments import Comment

class Reply(models.Model):
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.CharField(Comment,max_length=255,on_delete=models.CASCADE)
    reply = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)