from django.db import models
from .project import Project
#from .user import User

class Donation(models.Model):
    #user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount_of_donation = models.FloatField()