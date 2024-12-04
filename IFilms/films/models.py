from django.db import models

class FilmGenre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class FilmYear(models.Model):
    name = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class FilmStudio(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class FilmDirector(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class FilmCountry(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=128, unique=True)
    studio = models.ForeignKey(to=FilmStudio, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    year = models.ForeignKey(to=FilmYear, on_delete=models.CASCADE)
    director = models.ForeignKey(to=FilmDirector, on_delete=models.CASCADE)
    country = models.ForeignKey(to=FilmCountry, on_delete=models.CASCADE)
    screenplay = models.CharField(max_length=128, unique=True)
    genre = models.ForeignKey(to=FilmGenre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f'Фільм: {self.name} | Режисера: {self.director.name}'