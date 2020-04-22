from django.shortcuts import render
from movies.models import Movie

# Create your views here.

def do_search(request):
    movies = Movie.objects.filter(name__icontains=request.GET['q'])
    return render(request, "movies.html", {"movies":movies})