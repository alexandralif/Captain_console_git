from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from SearchHistory.models import Product_history


@login_required
def index(request):
    '''this functions gets the search history'''
    search_info = Product_history.objects.filter(user=request.user).all()
    return render(request, 'history/search_history.html', {
        'search_info': search_info,
    })


@login_required
def clear_search_history(request):
    '''this functions clears out the search history'''
    Product_history.objects.filter(user_id=request.user.id).delete()
    context = {}
    return render(request, 'history/search_history.html', context)
