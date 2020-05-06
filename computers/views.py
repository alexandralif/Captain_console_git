from django.shortcuts import render, get_object_or_404
from computers.models import computers

def index(request):
    context = {'computers': computers.objects.all().order_by('name')}
    return render(request, "computers/index.html", context)

def get_computer_by_id(request,id):
    return render(request, 'computers/computer_details.html', {
        'computers': get_object_or_404(computers, pk=id)
    })

