from django.shortcuts import render
from computers.models import computers

def index(request):
    context = {'computers': computers.objects.all().order_by('name')}
    return render(request, "computers/index.html", context)

