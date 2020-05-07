from django.shortcuts import render

from cart.models import Cart

def index(request):
    cart = Cart.objects.all()
    context = {'cart': cart}
    template = "cart/index.html"
    return render(request, context, template)






# Create your views here.
