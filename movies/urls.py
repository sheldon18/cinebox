from django.conf.urls import url, include
from .views import all_movies

urlpatterns = [
    url(r'^$', all_movies, name='movies'),
]