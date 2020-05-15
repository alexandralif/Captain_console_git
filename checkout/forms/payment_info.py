from django.forms import ModelForm,widgets
from checkout.models import payment
from django.forms import ValidationError

MONTH = [
    ('01', '01'),
('02', '02'),
('03', '03'),
('04', '04'),
('05', '05'),
('06', '06'),
('07', '07'),
('08', '08'),
('09', '09'),
('10', '10'),
('11', '11'),
('12', '12'),
]

YEAR = [
    ('20', '20'),
('21', '21'),
('22', '22'),
('23', '23'),
('24', '24'),
('25', '25'),
('26', '26'),
('27', '27'),
('28', '28'),

]


class PaymentForm(ModelForm):
    class Meta:
        model = payment
        exclude = [ 'user']
        widgets = {
            'cardholder' : widgets.TextInput(attrs={'class':'form-control'}),
            'card_num' : widgets.TextInput(attrs={'class':'form-control'}),
            'exp_month' : widgets.Select(choices=MONTH),
            'exp_year' : widgets.Select(choices=YEAR),
            'cvc' : widgets.NumberInput(attrs={'class':'form-control'}),
        }


