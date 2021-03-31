from django.db import models

class Category(models.Model):
    #proj_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)

