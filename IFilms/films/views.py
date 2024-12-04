from django.shortcuts import render

from films.models import Film

def index(request):
    return render(request, 'films/index.html')

def film_page(request):
    return render(request, 'films/film-page.html')

def favourite(request):
    return render(request, 'films/favourite.html')

def search_page(request):
    context = {
        'title': 'Film search',
        'films': Film.objects.all(),
    }
    return render(request, 'films/search-page.html', context)