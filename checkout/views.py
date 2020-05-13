from django.shortcuts import render

# Create your views here.
from checkout.forms.personal_info_form import PersonalForm


#def index(request):
#    context = {}

 #   return render(request, 'checkout/index.html', context)

def add_personal_info(request):
    if request.method == 'POST':
        form = PersonalForm(data=request.POST)

    else:

        form = PersonalForm()
    return render(request, 'checkout/add_personal_info.html', {
        'form': form
    })
def payment(request):
    context = {}
    return render(request, 'checkout/payment.html', context)

def review(request):
    context = {}
    return render(request, 'checkout/review.html', context)

