from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Movie, get_object_or_404

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    # output = ','.join([m.title for m in movies])
    # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1984)
    # select * from movies_movie where
    # Movie.objects.get(id=1)
    # return HttpResponse(output)


def detail(request, movie_id):
    # try:
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
