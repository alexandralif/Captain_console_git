from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from products.models import products
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


@login_required
def index(request):
    user = User.objects.filter(pk=request.user.id).first()
    cart = Cart.objects.filter(user=user)
    context = {'cart': cart.order_by('products')}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request, id):
    '''this is our add to cart function. It adds a product to the cart'''
    p=products.objects.filter(pk=id).first()
    u=User.objects.filter(pk=request.user.id).first()
    cart=Cart.objects.filter(user=u, products=p).first()
    if cart!=None: #if there item is already in the cart we only
        cart.quantity +=1 #have to expand the quantity by one
        cart.save()
    else: #if the item is not in the cart we have to add the entire item to the cart

        new_cart = Cart(user=u, products=p,quantity=1)
        new_cart.save()
        context = {}

    return redirect(index)


@login_required
def remove_from_cart(request,id):
    '''this is our remove from cart function. It removes single instance of a product from the
    cart.'''
    p = products.objects.filter(pk=id).first()
    u = User.objects.filter(pk=request.user.id).first()
    cart = Cart.objects.filter(user=u, products=p).first()
    print(id)
    print(p)
    print(u)
    print(cart)
    if cart.quantity > 1: #if the quantity of the product is bigger than one
        cart.quantity -=1 #we only have to lower the quantity and remove one of that item
        cart.save()
    else:      #else we have to delet the entire item from the cart
        cart.delete()
    return redirect(index)


@login_required
def clear_cart(request):
    '''this is our clear cart function. It clears the cart when the order is comfermed.'''
    Cart.objects.filter(user_id=request.user.id).delete()
    context = {}
    return render(request, 'cart/index.html', context)





