from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="front_page-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path("ordered_by_price", views.ordered_by_price, name="ordered_by_price"),
    path("ordered_by_name", views.ordered_by_name, name="ordered_by_name")

]
