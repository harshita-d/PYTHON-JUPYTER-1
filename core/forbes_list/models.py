from django.db import models


# Create your models here.
class forbesListModel(models.Model):
    Name = models.CharField(max_length=200, blank=False)
    Pay_USD = models.IntegerField(blank=False)
    Year = models.IntegerField(blank=False)
    Category = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.Name
