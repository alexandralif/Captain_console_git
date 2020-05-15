from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from checkout.models import personal_info, Order, Order_item
from cart.models import Cart
from checkout.forms.payment_info import PaymentForm
from checkout.models import payment
from checkout.forms.personal_info_form import PersonalForm
from products.models import products





def add_personal_info(request):
    #u = User.objects.filter(pk=request.user.id).first()
    #pers_info = personal_info.objects.filter(user=u).first()
    profile = personal_info.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PersonalForm(data=request.POST,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            #return redirect('checkout/payment')
    else:
        form = PersonalForm()
    return render(request, 'checkout/add_personal_info.html', {
        'form': form
    })
def payment_info(request):
    profile = payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentForm(data=request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # return redirect('checkout/payment')
    else:
        form = PaymentForm()

    return render(request, 'checkout/payment.html', {
        'form': form
    })


def review(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            #p = products.objects.filter(id=request.user.id).first()
            #u = User.objects.filter(pk=request.user).first()
            #product_cart = Cart.objects.filter(user=u, products=p).first()
            payment_info = payment.objects.filter(user=request.user).first()
            #product_cart = Cart.objects.filter(user=request.user).first()
            #items = Cart.objects.filter(user_id=request.user.id)
            pers_info = personal_info.objects.filter(user=request.user).first()
            user = User.objects.filter(pk=request.user.id).first()
            product_cart = Cart.objects.filter(user=request.user)
            #search_info = Product_history.objects.filter(user=request.user).all()


    return render(request, 'checkout/review.html', {
        'payment_info': payment_info,
        #'product_cart' :product_cart,
        'product_cart': product_cart,
        'pers_info': pers_info,
        #'products':get_object_or_404(products, id=reques)
    })


def ordered(request):
    if request.user.is_authenticated:
        payment_info = payment.objects.filter(user=request.user).first()
        pers_info = personal_info.objects.filter(user=request.user).first()
        create_order = Order(user=request.user,info=pers_info,confirmed=True,payment=payment_info)
        create_order.save()
        cart = Cart.objects.filter(user=request.user)
        for item in cart:
            product = products.objects.get(pk=item.products.id)
            order_product = Order_item(order_id=create_order.id,products_id=product.id,quantity=item.quantity)
            order_product.save()

    Cart.objects.filter(user_id=request.user.id).delete()

    context = {}
    return render(request,'checkout/order_success.html',context)
