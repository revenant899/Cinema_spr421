from django.shortcuts import render

from favorites.favorites import get_favorite_films
from films.models import Film



def index(request, filter_by_favorites=False):
    films = Film.objects.all()

    filter_text = request.GET.get("filter_text", "")

    if filter_by_favorites:
        fav_ids = get_favorite_films(request)
        films = films.filter(id__in=fav_ids)

    if filter_text:
        films = films.filter(name__icontains=filter_text)

    return render(request, 'home/index.html', {
        'films': films, 
        "fav_ids": get_favorite_films(request),
    })