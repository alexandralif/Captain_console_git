from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name="remove_from_cart"),
]
