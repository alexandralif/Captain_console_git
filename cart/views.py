from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from products.models import products
from django.shortcuts import render


@login_required
def index(request):
    context = {'cart': Cart.objects.all().order_by('products')}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request, id):
    print(id)
    return render(request, 'products/product_details.html', {
       'products': get_object_or_404(products, pk=id)
    })


