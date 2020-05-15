from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from checkout.models import Order


class account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class account_image(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(account, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class order_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
