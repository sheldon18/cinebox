from django.shortcuts import render
from .models import Movie


# Create your views here.
def all_movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {"movies": movies})