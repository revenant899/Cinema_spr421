from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from films.forms.film import FilmForm
from films.models import Film


def admin_list(request):
    films = Film.objects.all()
    return render(request, 'films/adminlist.html', {'films': films})


def film_detail(request, film_id):
    films = Film.objects.all()
    return render(request, 'films/detail.html', {'film': films[film_id - 1]})

def film_delete(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    film.delete()
    messages.error(request, f"Film deleted successfully!")
    return redirect('admin_list')

def film_create(request):
    if request.method == "POST":
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
            messages.success(request, "Film created successfully!")
            return redirect("/films/adminList/")
    else:
        film_form = FilmForm()

    return render(request, 'films/create.html', {'form': film_form})

def film_update(request, film_id):
    film = get_object_or_404(Film, pk=film_id)

    if request.method == "POST":
        film_form = FilmForm(request.POST, request.FILES, instance=film)
        if film_form.is_valid():
            film_form.save()
            messages.success(request, "Film updated successfully!")
            return redirect("/films/adminList/")
    else:
        film_form = FilmForm(instance=film)

    return render(request, 'films/update.html', {'form': film_form, 'film': film})