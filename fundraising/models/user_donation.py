from django.db import models
from .project import Project
from accounts.models import MyUser

class Donation(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount_of_donation = models.FloatField()