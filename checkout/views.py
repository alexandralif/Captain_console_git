from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'checkout/index.html', context)


def payment(request):
    context = {}
    return render(request, 'checkout/payment.html', context)

def review(request):
    context = {}
    return render(request, 'checkout/review.html', context)