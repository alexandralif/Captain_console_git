from django.shortcuts import render
from games.models import games


def index(request):
    return render(request, "games/index.html", {
        'games': games.objects.all()
    })

