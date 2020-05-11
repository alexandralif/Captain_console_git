from django.contrib.auth.models import User
from django.db import models

from products.models import products
from computers.models import computers




class Cart(models.Model):
    products = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.FloatField()






