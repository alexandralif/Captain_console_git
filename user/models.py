from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_img = models.CharField(max_length=999,default="https://img.icons8.com/material-outlined/24/000000/user--v1.png")