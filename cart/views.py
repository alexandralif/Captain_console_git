from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from products.models import products


@login_required
def index(request):
    user = User.objects.filter(pk=request.user.id).first()
    cart = Cart.objects.filter(user=user)
    context = {'cart': cart.order_by('products')}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request, id):
    p=products.objects.filter(pk=id).first()
    u=User.objects.filter(pk=request.user.id).first()
    cart=Cart.objects.filter(user=u, products=p).first()
    if cart!=None:
        cart.quantity +=1
        cart.save()
    else:
        #c=Cart.objects.filter(user=u,products=p,quantity=1).first()
        new_cart = Cart(user=u, products=p,quantity=1)
        new_cart.save()
    return render(request, 'products/product_details.html', {
       'products': get_object_or_404(products, pk=id)
    })

@login_required
def remove_from_cart(request,id):
    #cart_item= get_object_or_404(cart,pk=id)
    #cart_item.delete()

    p = products.objects.filter(pk=id).first()
    u = User.objects.filter(pk=request.user.id).first()
    cart = Cart.objects.filter(user=u, products=p,).first()
    if cart.quantity > 1:
        cart.quantity -=1
        cart.save()
    else:
        cart.delete()
    #return render(request, 'cart/index.html', {
    #    'products': get_object_or_404(products, pk=id)
    #})
    return render(request, 'products/product_details.html', {
        'products': get_object_or_404(products, pk=id)
    })

#def delete_all_cart()




