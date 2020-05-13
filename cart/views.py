from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from products.models import products


@login_required
def index(request):
    context = {'cart': Cart.objects.all().order_by('products')}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request, id):
    print(id)
    p=products.objects.filter(pk=id).first()
    u=User.objects.filter(pk=request.user.id).first()
    cart=Cart.objects.filter(user=u, products=p).first()
    if cart!=None:
        cart.quantity +=1
        cart.save()
    else:
        c=Cart(user=u,products=p,quantity=1)
        c.save()
    return render(request, 'products/product_details.html', {
       'products': get_object_or_404(products, pk=id)
    })

#def remove_from_cart(request,id):

