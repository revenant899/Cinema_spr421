FAVORITE_FILMS_KEY = 'favorite_list'

def get_favorite_films(request):
    return request.session.get(FAVORITE_FILMS_KEY, [])

def get_count_of_favorite_films(request):
    return len(get_favorite_films(request))

def add_film_to_favorites(request, film_id):
    favoriteIds = get_favorite_films(request)
    if film_id not in favoriteIds:
        favoriteIds.append(film_id)
        request.session[FAVORITE_FILMS_KEY] = favoriteIds
    request.session.modified = True

def remove_film_from_favorites(request, film_id):
    favoriteIds = get_favorite_films(request)
    if film_id in favoriteIds:
        favoriteIds.remove(film_id)
        request.session[FAVORITE_FILMS_KEY] = favoriteIds
    request.session.modified = True