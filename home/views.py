from django.shortcuts import render

from favorites.favorites import get_count_of_favorite_films, get_favorite_films
from films.models import Film



def index(request, filter_by_favorites=False):
    films = Film.objects.all()

    if filter_by_favorites:
        fav_ids = get_favorite_films(request)
        films = films.filter(id__in=fav_ids)

    return render(request, 'home/index.html', {
        'films': films, 
        "fav_count": get_count_of_favorite_films(request),
        "fav_ids": get_favorite_films(request),
    })