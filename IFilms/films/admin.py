from django.contrib import admin

from films.models import Film, FilmGenre, FilmYear, FilmStudio, FilmDirector, FilmCountry

admin.site.register(Film)
admin.site.register(FilmGenre)
admin.site.register(FilmYear)
admin.site.register(FilmStudio)
admin.site.register(FilmDirector)
admin.site.register(FilmCountry)
