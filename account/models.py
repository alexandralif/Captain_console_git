from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from checkout.models import Order


class account(models.Model):
    '''this is our account model class. We create it so that we can allow the user to add more information
    about them.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class account_image(models.Model):
    '''this is our account image model class. We created it so that the user can have a photo
    on his profile.'''
    image = models.CharField(max_length=999)
    user = models.ForeignKey(account, on_delete=models.CASCADE)

    def __str__(self):
        return self.image



