from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms.create_user import ProfileCreateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm(),

    })

def get_user_by_id(request,id):
    return render(request, 'user/my_account.html', {
        'user': get_object_or_404(User, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        user = [{
            'id': x.id,
            'name': x.name,
        } for x in User.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': user})
    context = {'computers': User.objects.all().order_by('name')}
    return render(request, "user/my_account.html", context)

#@login_required
def create_user(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ProfileCreateForm()
    return render(request, 'user/create_user.html', {
        'form': form
    })
