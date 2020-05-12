from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='checkout-index'),
    path('payment/',views.payment,name='checkout-payment'),
    path('review/',views.review, name='checkout-review')
]

