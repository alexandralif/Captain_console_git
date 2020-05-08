from django.db import models

# Create your models here.
from computers.models import computers
from front_page.models import products


class Cart(models.Model):
    products = models.ManyToManyField(products,  null=True, blank=True)
    total_price = models.FloatField()





