from django.shortcuts import render, get_object_or_404
from games.models import games


def index(request):
    return render(request, "games/index.html", {
        'games': games.objects.all()
    })

def get_game_by_id(request,id):
    return render(request, 'games/game_details.html', {
        'computers': get_object_or_404(games, pk=id)
    })
