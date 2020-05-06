from django.shortcuts import render, get_object_or_404
from games.models import games


def index(request):
    return render(request, "games/index.html", {
        'games': games.objects.all()
    })

<<<<<<< HEAD
def get_game_by_id(request,id):
    return render(request, 'games/game_details.html', {
        'computers': get_object_or_404(games, pk=id)
    })
=======
>>>>>>> 60cc43c89f015f5c136754f4cbdb7168176ae841
