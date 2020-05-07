from django.shortcuts import render
from computers.models import computers


def index(request):
    return render(request, "front_page/index.html")


# Create your views here.
