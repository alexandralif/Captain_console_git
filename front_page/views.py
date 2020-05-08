from django.shortcuts import render, get_object_or_404
from front_page.models import products

def index(request):
    context ={'products': products.objects.all().order_by('name')}
    return render(request, "front_page/index.html", context)

def get_product_by_id(request,id):
    return render(request, 'front_page/product_details.html', {
        'products': get_object_or_404(products, pk=id)
    })
# Create your views here.
