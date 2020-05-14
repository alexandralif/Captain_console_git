from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from checkout.models import personal_info
from cart.models import Cart
from checkout.forms.payment_info import PaymentForm
from checkout.models import payment
from checkout.forms.personal_info_form import PersonalForm





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
            payment_info = payment.objects.filter(user=request.user).first()
            product_cart = Cart.objects.filter(user=request.user).first()
            pers_info = personal_info.objects.filter(user=request.user).first()

    return render(request, 'checkout/review.html', {
        'payment_info': payment_info,
        'product_cart' :product_cart,
        'pers_info': pers_info,
    })

