from django.db import models
from .project import Project
from accounts.models import MyUser

class Rate(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    proj_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    number_of_users = models.IntegerField()
    individual_rate = models.IntegerField()
    total_rate = models.FloatField()
    overall_avg_rating = models.FloatField()