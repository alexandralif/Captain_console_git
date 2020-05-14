from django.contrib.auth.models import User
from django.db import models


from products.models import products

class Cart(models.Model):
    '''this is our cart model. Here we create a model for all the information that we want to
    be displayed in the cart '''
    products = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.IntegerField(default=0)











