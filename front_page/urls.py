from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="front_page-index"),
    path('<int:id>', views.get_product_by_id, name="product_details")

]
