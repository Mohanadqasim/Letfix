from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.
class Movie(models.Model):
      id = models.CharField(max_length=255,primary_key=True )
      title = models.CharField(max_length=255, null=True, )
      release_date = models.CharField(max_length=255, null=True, )
      poster_path = models.CharField(max_length=255, null=True, )
      overview = models.TextField(max_length=2555, null=True, ) 
      watcher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
      
      def __str__(self):
            return self.title
      def get_absolute_url(self):
            return reverse('Movie_list')