from django.db import models
from computers.models import computer_catergory

# Create your models here.
class game_category(models.Model):
    name = models.CharField(max_length=255)

class games(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    game_category = models.ForeignKey(game_category, on_delete=models.CASCADE)
    computer_category = models.ForeignKey(computer_catergory, on_delete=models.CASCADE)
    onsale = models.BooleanField()
    description = description = models.CharField(max_length=999, blank=True)

class games_image(models.Model):
    image = models.CharField(max_length=999)
    games = models.ForeignKey(games, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
