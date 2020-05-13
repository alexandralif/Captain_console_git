from django.forms import ModelForm, widgets
from django import forms
from account.models import account

class ProfileCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = account
        exclude = ['id', 'user', 'image']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),

        }
