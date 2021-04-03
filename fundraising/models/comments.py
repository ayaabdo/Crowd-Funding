from django.db import models
from .project import Project
from accounts.models import MyUser

class Comment(models.Model):
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    # name = models.CharField(max_length=80)
    # email = models.EmailField()
    # body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['created_on']

    # def __str__(self):
    #     return 'Comment {} by {}'.format(self.body, self.name)