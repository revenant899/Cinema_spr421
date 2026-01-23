FAVORITE_FILMS_KEY = 'favorite_list'

def get_favorite_films(request):
    return request.session.get(FAVORITE_FILMS_KEY, [])

def get_count_of_favorite_films(request):
    return len(get_favorite_films(request))

def add_film_to_favorites(request, product_id):
    favoriteIds = get_favorite_films(request)
    if product_id not in favoriteIds:
        favoriteIds.append(product_id)
        request.session[FAVORITE_FILMS_KEY] = favoriteIds
    request.session.modified = True

def remove_film_from_favorites(request, product_id):
    favoriteIds = get_favorite_films(request)
    if product_id in favoriteIds:
        favoriteIds.remove(product_id)
        request.session[FAVORITE_FILMS_KEY] = favoriteIds
    request.session.modified = True