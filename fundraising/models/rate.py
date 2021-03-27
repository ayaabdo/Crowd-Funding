from django.db import models
from .project import Project

class Rate(models.Model):
    proj_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    number_of_users = models.IntegerField()
    individual_rate = models.IntegerField()
    total_rate = models.FloatField()
    overall_avg_rating = models.FloatField()