from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import Movie



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers



class ActionviewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(movie_type='Action')
    print(queryset)
    serializer_class = MovieSerializers
