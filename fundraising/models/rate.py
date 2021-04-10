from django.db import models
from .project import Project
from accounts.models import MyUser

class Rate(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    proj_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    individual_rate = models.IntegerField( null=True)
    # number_of_users = models.IntegerField( null=True,default=0)
    # total_rate = models.FloatField( null=True)
    # overall_avg_rating = models.FloatField( null=True)