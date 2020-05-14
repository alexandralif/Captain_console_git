from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name='checkout-index'),
    path('add_personal_info/',views.add_personal_info, name='checkout-add_personal_info'),
    path('payment/',views.payment_info,name='checkout-payment'),
    path('review/',views.review, name='checkout-review'),
    path('ordered/',views.ordered,name="checkout-ordered")

]

