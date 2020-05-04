from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank = True)
    year_of_start = models.DateTimeField()

