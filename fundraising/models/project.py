from django.db import models
from .categories import Category
from .tags import Tag
from accounts.models import MyUser

class Project(models.Model):
    user_ID = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    #images = models.ManyToManyField(Image)
    total_target = models.FloatField()
    total_donation = models.FloatField()

################ rate ##############
    number_of_users_rate = models.IntegerField( default=0)
    total_rate = models.IntegerField( default=0)
    overall_avg_rating = models.IntegerField( default=0)


    created_at = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    featured = models.BooleanField(default=False)
    #user_id