from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from SearchHistory.models import Product_history


def index(request):
    context = {}
    return render(request, 'history/search_history.html', context)

@login_required
def see_search_history(request):
    user_history = Product_history.objects.filter(user=request.user)
    pass
