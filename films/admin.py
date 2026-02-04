from django.contrib import admin

from films.models import Film

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'category']
    list_filter = ['category']

admin.site.register(Film, FilmAdmin)