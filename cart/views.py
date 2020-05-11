from django.contrib.auth.decorators import login_required
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
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        product = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstImage': x.product_image_set.first().image
        } for x in products.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': product})
    return render(request, 'products/product_details.html', {
       'products': get_object_or_404(products, pk=id)
    })
