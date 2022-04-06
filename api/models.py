# import imp
# from pkgutil import ImpImporter
# import resource
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.


class MoviesResoures(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        exclude = ['date_created']
