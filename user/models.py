from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class account_image(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(account, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
