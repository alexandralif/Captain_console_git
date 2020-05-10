from django.shortcuts import render, get_object_or_404
from games.models import games
from django.http import JsonResponse


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        game = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstImage': x.games_image_set.first().image
        } for x in games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': game})
    context = {'games': games.objects.all().order_by('name')}
    return render(request, "games/index.html", context)




def get_game_by_id(request,id):
    return render(request, 'games/game_details.html', {
        'games': get_object_or_404(games, pk=id)
    })

