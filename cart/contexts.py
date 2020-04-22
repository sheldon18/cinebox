from django.shortcuts import get_object_or_404
from movies.models import Movie


def cart_contents(request):
    """ Ensure that cart ontents are availble when rendering every page"""
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    movie_count = 0
    
    for id, quantity in cart.items():
        movie = get_object_or_404(Movie, pk=id)
        total += quantity * movie.price
        movie_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'movie': movie})
    
    return {'cart_items': cart_items, 'total': total, 'movie_count': movie_count}