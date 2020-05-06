from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method != 'POST':
        return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })
    else:
        form = UserCreationForm(data=request.POST)
        if form.valid():
            form.save()
            return redirect('login')

