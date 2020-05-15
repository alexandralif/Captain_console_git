from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from products.models import products
#from checkout.forms.payment_info import card_num

# Create your models here.
class personal_info(models.Model):
    '''this is our model for personal/shipping information when ordering a product'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_num = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

def card_num(value):
    if len(str(value)) != 16:
        raise ValidationError('Kortanúmer verður að vera af lengd 16')
    if value != int:
        raise ValidationError


def card_month(value):
    if len(str(value)) != 2:
        raise  ValidationError("Mánuður verður að vera af lengd 2")


class payment(models.Model):
    '''this is our payment model for paying for an order'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder = models.CharField(max_length=255)
    card_num = models.IntegerField(max_length=16,validators=[card_num])
    exp_month = models.IntegerField(max_length=2,validators=[card_month],default="MM")
    exp_year = models.IntegerField(max_length=2)
    cvc = models.IntegerField(max_length=3)

class Order(models.Model):
    '''this is our oredr model'''
    user = models.ForeignKey(personal_info, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    payment = models.ForeignKey(payment, on_delete=models.CASCADE)

class Order_item(models.Model):
    products = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

