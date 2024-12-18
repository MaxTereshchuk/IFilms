from django.contrib import admin

from films.models import Film, FilmGenre, FilmYear, FilmStudio, FilmDirector, FilmCountry

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'studio', 'year', 'director')
    search_fields = ('name', 'director__name')
    ordering = ('name',)

@admin.register(FilmYear)
class YearAdmin(admin.ModelAdmin):
    ordering = ('-name',)

@admin.register(FilmGenre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(FilmStudio)
class StudioAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(FilmDirector)
class DirectorAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(FilmCountry)
class CountryAdmin(admin.ModelAdmin):
    ordering = ('name',)