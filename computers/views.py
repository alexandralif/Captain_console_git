from django.shortcuts import render, get_object_or_404
from computers.models import computers
from django.http import JsonResponse

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        computer = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstImage': x.computer_image_set.first().image
        } for x in computers.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': computer})
    context = {'computers': computers.objects.all().order_by('name')}
    return render(request, "computers/index.html", context)


def get_computer_by_id(request,id):
    return render(request, 'computers/computer_details.html', {
        'computers': get_object_or_404(computers, pk=id)
    })

