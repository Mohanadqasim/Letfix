from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Movie(models.Model):
      id = models.CharField(max_length=255,primary_key=True )
      title = models.CharField(max_length=255, null=True, )
      release_date = models.CharField(max_length=255, null=True, )
      poster_path = models.CharField(max_length=255, null=True, )
      overview = models.TextField(max_length=2555, null=True, ) 
      watcher = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
