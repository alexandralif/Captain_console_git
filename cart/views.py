from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from front_page.models import products


@login_required
def index(request):
    context = {'cart': Cart.objects.all().order_by('products')}
    return render(request, 'cart/index.html', context)

#@login_required
def add_to_cart(request, id):
    print('hæhæ')
    return render(request, 'front_page/product_details.html', {
        'products': get_object_or_404(products, pk=id)
    })

# Create your views here.
