from django.db import models

# Create your models here.
from django.db.models import ForeignKey

from games.models import games

class computer_category(models.Model):
    name = models.CharField(max_length=255)

class computers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(computer_category, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    games = models.ForeignKey(games, on_delete=models.CASCADE)

class computer_image(models.Model):
    image = models.CharField(max_length=999)
    computers = models.ForeignKey(computers, on_delete=models.CASCADE)
    def __str__(self):
        return self.image



