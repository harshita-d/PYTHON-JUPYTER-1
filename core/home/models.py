from django.db import models


class PlatformList(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class MovieList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=500)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    # platform = models.ForeignKey(PlatformList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
