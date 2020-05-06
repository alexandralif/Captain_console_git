from django.shortcuts import render
from games.models import games


def index(request):
<<<<<<< HEAD
    return render(request, "games/index.html")


=======
    return render(request, "games/index.html", {
        'games': games.objects.all()
    })
>>>>>>> 4a440566964b23a05c86190a3235720a99caf2fa
