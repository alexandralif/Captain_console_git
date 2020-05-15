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

#@login_required
def create_user(request):
    '''this function creates a new user and allows the user to update their profile.'''
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
    else:
        form = ProfileCreateForm()
    return render(request, 'user/create_user.html', {
        'form': form,
    })

@login_required
def show_user(request):
    '''this function allows the user to see their information'''
    account_info = account.objects.filter(user=request.user).first()
    return render(request,'user/my_account.html',{
        'account_info':account_info
    })

@login_required
def order_history(request):
    '''this function allows the user to see their order history'''
    u = User.objects.filter(pk=request.user.id).first() #here we are getting the user id
    users_order = Order.objects.filter(user=u).all() #here we are getting the orders that belong to the id
    orders = []
    for order in users_order:
        order_item_instances = Order_item.objects.filter(order=order).all() #here we are getting a single order
        products_ = []
        for instance in order_item_instances: #here we are itterating through the items in that order
            p = products.objects.filter(pk=instance.products.id).first() #here we are getting a single product in the order
            products_.append(p) #we append that product to our product list
        orders.append(products_)  #and then we append our product list to our order list
    return render(request,'user/order_history.html',{
        'orders': orders,
    })





