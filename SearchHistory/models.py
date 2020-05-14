from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from products.models import products


class Product_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


