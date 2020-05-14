from django.forms import ModelForm,widgets
from checkout.models import payment

class PaymentForm(ModelForm):
    class Meta:
        model = payment
        exclude = [ 'user']
        widgets = {
            'cardholder' : widgets.TextInput(attrs={'class':'form-control'}),
            'card_num' : widgets.NumberInput(attrs={'class':'form-control'}),
            'exp_month' : widgets.NumberInput(attrs={'class':'form-control'}),
            'exp_year' : widgets.NumberInput(attrs={'class':'form-control'}),
            'cvc' : widgets.NumberInput(attrs={'class':'form-control'}),
        }