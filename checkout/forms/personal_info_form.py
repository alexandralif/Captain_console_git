from django.forms import ModelForm,widgets

from checkout.models import personal_info


class PersonalForm(ModelForm):
    class Meta:
        model = personal_info
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'} ),
            'street-name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house-num': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class':'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
        }