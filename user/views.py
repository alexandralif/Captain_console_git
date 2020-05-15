from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.models import account
from account.models import account_image
from checkout.models import Order, Order_item
from products.models import products
from user.forms.create_user import ProfileCreateForm
from django.contrib.auth.decorators import login_required



def register(request):
    '''this functions reqisters a new user'''
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm(),

    })

def get_user_by_id(request,id):
    '''this functions gets the user by id'''
    return render(request, 'user/my_account.html', {
        'user': get_object_or_404(User, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        user = [{
            'id': x.id,
            'name': x.name,
        } for x in User.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': user})
    context = {'computers': User.objects.all().order_by('name')}
    return render(request, "user/my_account.html", context)

#@login_required
def create_user(request):
    '''this function creates a new user with additional info'''
    profile = account.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileCreateForm(data=request.POST, instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            created = form.save()
            acc_img = account_image(image=request.POST['image'], user = created)
            acc_img.save()
            #return redirect('user/my_account')
    else:
        form = ProfileCreateForm()
    return render(request, 'user/create_user.html', {
        'form': form,
    })


@login_required
def show_user(request):
    '''this show the users information'''
    account_info = account.objects.filter(user=request.user).first()
    account_photo = account_image.objects.filter(user=account_info).first()

    return render(request,'user/my_account.html',{
        'account_info':account_info
    })

@login_required
def order_history(request):
    '''this show the users order history'''
    u = User.objects.filter(pk=request.user.id).first()

    users_order = Order.objects.filter(user=u).all()
    orders = []
    for order in users_order:
        order_item_instances = Order_item.objects.filter(order=order).all()
        products_ = []
        for instance in order_item_instances:
            p = products.objects.filter(pk=instance.products.id).first()
            products_.append(p)
        orders.append(products_)


    return render(request,'user/order_history.html',{
        'orders': orders,
    })





