from django.shortcuts import render

computers = [
    {'name': 'Macbook', 'price': '1000'},
    {'name': 'Macbook Pro', 'price': '1100'}
]
# Create your views here.
def index(request):
    return render(request, "computers/index.html", context={'computers' : computers})

