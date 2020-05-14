from django.shortcuts import render, get_object_or_404
from products.models import products
from django.http import JsonResponse

def index(request):
    '''this function allows the user to search a product by a name!'''
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        product = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstImage': x.product_image_set.first().image
        } for x in products.objects.filter(name__icontains=search_filter)]
        print(product)
        return JsonResponse({'data': product})
    context ={'products': products.objects.all().order_by('name')}
    return render(request, "products/index.html", context)

def get_product_by_id(request,id):
    return render(request, 'products/product_details.html', {
        'products': get_object_or_404(products, pk=id)
    })

def get_all_games(request):
    '''this is a function that groups all the games in one'''
    context = {'products': products.objects.filter(type_id=2)}
    return render(request, "products/index.html", context)

def get_all_computers(request):
    '''this is a function that groups all the computers in one'''
    context = {'products': products.objects.filter(type_id=1)}
    return render(request, "products/index.html", context)

def ordered_by_price(request):
    '''this is a function that orders the products by price'''
    context = {'products': products.objects.all().order_by('price')}
    return render(request, "products/index.html", context)


def ordered_by_name(request):
    '''this is product that orders the products by name'''
    context = {'products': products.objects.all().order_by('name')}
    return render(request, "products/index.html", context)

def get_nintendo_products(request):
    '''this function get's all products that have the same manufacturer'''
    context = {'products': products.objects.filter(category_id=1)}
    return render(request, "products/index.html", context)

def get_gameboy_products(request):
    '''this function get's all products that have the same manufacturer'''
    context = {'products': products.objects.filter(category_id=2)}
    return render(request, "products/index.html", context)

def get_playstation_products(request):
    '''this function get's all products that have the same manufacturer'''
    context = {'products': products.objects.filter(category_id=3)}
    return render(request, "products/index.html", context)

def get_xbox_products(request):
    '''this function get's all products that have the same manufacturer'''
    context = {'products': products.objects.filter(category_id=4)}
    return render(request, "products/index.html", context)
