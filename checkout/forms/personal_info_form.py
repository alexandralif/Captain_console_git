from django.forms import ModelForm,widgets

from checkout.models import personal_info
from django.forms import ValidationError


from django import forms
COUNTRIES = [
    ('iceland', 'Iceland'),
    ('denmark', 'Denmark'),
    ('norway', 'Norway'),
    ('sweden', 'Sweden'),
    ('england', 'England'),
    ('finland', 'Finland'),
    ('germany', 'Germany'),
]

class PersonalForm(ModelForm):
    class Meta:
        model = personal_info
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'} ),
            'street-name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house-num': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(choices=COUNTRIES),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


    #class cleanUrlForm(forms.form):
     #   url =

    def check_streetname(self):
        street_name = self.cleaned_data['street-name']
        if len(street_name)<4:
            raise forms.ValidationError('street not exist')
        return street_name