from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from computers.models import computers
from front_page.models import products



class Cart(models.Model):
    products = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.FloatField()






