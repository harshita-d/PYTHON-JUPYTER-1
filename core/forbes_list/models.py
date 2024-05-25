from django.db import models


# Create your models here.
class forbesListModel(models.Model):
    Name = models.CharField(max_length=200)
    Pay_USD = models.IntegerField()
    Year = models.IntegerField()
    Category = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
