from django.forms import ModelForm,widgets
from checkout.models import personal_info

from django import forms
COUNTRIES = [
    ('iceland', 'Iceland'),
    ('denmark', 'Denmark'),
    ('norway', 'Norway'),
    ('sweden', 'Sweden'),
    ('england', 'England'),
    ('finland', 'Finland'),
    ('germany', 'Germany'),
    ('poland','Poland'),
    ('italy','Italy'),
]

class PersonalForm(ModelForm):
    '''This is a form for the personal information that the user puts in'''
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
