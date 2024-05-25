from django.db import models


class PlatformList(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class MovieList(models.Model):
    Poster_Link = models.URLField(max_length=100)
    Series_Title = models.CharField(max_length=100)
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
    Gross = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    # platform = models.ForeignKey(PlatformList, on_delete=models.CASCADE)

    def __str__(self):
        return self.Poster_Link
