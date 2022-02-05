from email.policy import default
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=100, default='drame')

    def __str__(self) :
        return  self.name
