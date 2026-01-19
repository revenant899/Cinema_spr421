from django.shortcuts import render

from films.models import Film



def index(request):
    films = Film.objects.all()
    return render(request, 'home/index.html', {'films': films})