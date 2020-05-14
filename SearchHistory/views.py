from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from SearchHistory.models import Product_history


@login_required
def index(request):
    context = {}
    return render(request, 'history/search_history.html', context)

