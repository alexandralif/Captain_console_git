from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from products.models import products
#from checkout.forms.payment_info import card_num



def zip_info(value):
    '''this is a function that validates the zip info'''
    try:
        int(value)
    except ValueError:
        raise ValidationError('Einungis hægt að slá inn tölustafi')



# Create your models here.
class personal_info(models.Model):
    '''this is our model for personal/shipping information when ordering a product'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_num = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255,validators=[zip_info])

def card_num(value):
    '''this is a function that validates the cardnumber that the user inputs'''
    if len(str(value)) != 16:
        raise ValidationError('Kortanúmer verður að vera af lengd 16')

def cvc_num(value):
    '''this is a function that validates the CVC that the user inputs'''
    if len(str(value)) != 3:
        raise ValidationError('CVC verður að vera af lengd 3')




class payment(models.Model):
    '''this is our payment model for paying for an order'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder = models.CharField(max_length=255)
    card_num = models.CharField(max_length=255,validators=[card_num])
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3,validators=[cvc_num])

class Order(models.Model):
    '''this is our order model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.ForeignKey(personal_info, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    payment = models.ForeignKey(payment, on_delete=models.CASCADE)

class Order_item(models.Model):
    '''this is the model that saves the products in orders'''
    products = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

