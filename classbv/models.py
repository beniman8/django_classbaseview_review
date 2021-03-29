from django.db import models

# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=50)
    count = models.IntegerField(null=True)
