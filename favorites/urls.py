from django.urls import path
from django.contrib import admin

import favorites.views

urlpatterns = [
    path('add/<int:film_id>/<str:return_url>/', favorites.views.add_film, name='add_fav_film'),
    path('remove/<int:film_id>/<str:return_url>/', favorites.views.remove_film, name='remove_fav_film'),
]