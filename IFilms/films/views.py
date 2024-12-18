from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from films.models import Film, FilmGenre, FilmYear, FilmStudio, FilmDirector, FilmCountry, FavouriteFilm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'films/index.html', context)

def film_page(request, film_id):
    film = Film.objects.get(id=film_id)
    if request.user.is_authenticated:
        is_favourite = FavouriteFilm.objects.filter(user=request.user, film=film).exists()
    else:
        is_favourite = False

    context = {
        'title': 'Film page',
        'film': film,
        'is_favourite': is_favourite,
    }

    return render(request, 'films/film-page.html', context)
@login_required
def favourite(request):
    films = Film.objects.filter(favouritefilm__user=request.user)
    context = {
        'title': 'Favourite film page',
        'films': films,
    }
    return render(request, 'films/favourite.html', context)

@login_required
def toggle_favourite(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    user = request.user

    favourite = FavouriteFilm.objects.filter(user=user, film=film).first()

    if favourite:
        favourite.delete()
        added_to_fav = False
    else:
        FavouriteFilm.objects.create(user=user, film=film, heart_image='heart.svg')
        added_to_fav = True

    return JsonResponse({'added_to_fav': added_to_fav})
def search_page(request):
    query = request.GET.get('query', '')
    genre_ids = request.GET.getlist('genre')
    year_ids = request.GET.getlist('year')
    studio_ids = request.GET.getlist('studio')
    director_ids = request.GET.getlist('director')
    country_ids = request.GET.getlist('country')

    films = Film.objects.filter(
        Q(name__icontains=query) | Q(director__name__icontains=query) | Q(studio__name__icontains=query)
    )

    if genre_ids and '' not in genre_ids:
        films = films.filter(genre_id__in=genre_ids)
    if year_ids and '' not in year_ids:
        films = films.filter(year_id__in=year_ids)
    if studio_ids and '' not in studio_ids:
        films = films.filter(studio_id__in=studio_ids)
    if director_ids and '' not in director_ids:
        films = films.filter(director_id__in=director_ids)
    if country_ids and '' not in country_ids:
        films = films.filter(country_id__in=country_ids)

    first_page = 1
    paginator = Paginator(films, 12)
    page_number = request.GET.get('page', first_page)
    page_obj = paginator.page(page_number)

    context = {
        'title': 'Film search',
        'films': films,
        'query': query,
        'genres': FilmGenre.objects.all(),
        'years': FilmYear.objects.all(),
        'studios': FilmStudio.objects.all(),
        'directors': FilmDirector.objects.all(),
        'countries': FilmCountry.objects.all(),
        'selected_genres': genre_ids,
        'selected_years': year_ids,
        'selected_studios': studio_ids,
        'selected_directors': director_ids,
        'selected_countries': country_ids,
        'page_obj': page_obj,
    }
    return render(request, 'films/search-page.html', context)

def base_page(request):
    query = request.GET.get('query', '')
    films = Film.objects.filter(
        Q(name__icontains=query) | Q(director__name__icontains=query) | Q(studio__name__icontains=query)
    )

    context = {
        'films': films,
        'query': query,
    }
    return render(request, 'films/base.html', context)