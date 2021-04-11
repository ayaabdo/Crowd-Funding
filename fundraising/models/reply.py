from django.db import models
from .project import Project
from accounts.models import MyUser
from .comments import Comment

class Reply(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, max_length=255, on_delete=models.CASCADE,related_name='replies')
    reply = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)