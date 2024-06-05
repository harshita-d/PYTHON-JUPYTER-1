from django.db import models

# Create your models here.


class MovieList(models.Model):
    id = models.AutoField(primary_key=True)
    poster_link = models.URLField(max_length=100)
    title = models.CharField(max_length=100)
    Released_Year = models.IntegerField()
    Certificate = models.CharField(max_length=100)
    Runtime = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    IMDB_Rating = models.IntegerField()
    Overview = models.CharField(max_length=1000)
    Director = models.CharField(max_length=100)
    Star1 = models.CharField(max_length=100)
    Star2 = models.CharField(max_length=100)
    Star3 = models.CharField(max_length=100)
    Star4 = models.CharField(max_length=100)
    Gross = models.IntegerField()

    def __str__(self):
        return self.title


class moviesData(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, unique=True)
    poster_link = models.URLField()
    genre = models.ManyToManyField("genreData", related_name="movies_data")

    def __str__(self):
        return self.title


class genreData(models.Model):

    genre_type = models.CharField(max_length=200, unique=True, default="")

    def __str__(self):
        return self.genre_type
