from django.db import models

# Create your models here.
from computers.models import computers
from games.models import games


class Cart(models.Model):
    game_products = models.ManyToManyField(games,  null=True, blank=True)
    computer_products = models.ManyToManyField(computers,  null=True, blank=True)
    total_price = models.FloatField()

