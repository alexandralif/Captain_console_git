from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_img = models.CharField(max_length=999,default='https://icons8.com/icon/82751/user')