from django.urls import path

import favorites.views

urlpatterns = [
    path('add/<int:film_id>/', favorites.views.add_film, name='add_fav_film'),
    path('remove/<int:film_id>/', favorites.views.remove_film, name='remove_fav_film'),
]