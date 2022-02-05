from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Movie
        fields = ['id', 'name', 'duration', 'rating', 'movie_type']