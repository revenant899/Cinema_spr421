from django.shortcuts import redirect, render
from favorites.favorites import add_film_to_favorites, remove_film_from_favorites

def add_film(request, film_id, return_url):
    add_film_to_favorites(request, film_id)
    return redirect(return_url)

def remove_film(request, film_id, return_url):
    remove_film_from_favorites(request, film_id)
    return redirect(return_url)