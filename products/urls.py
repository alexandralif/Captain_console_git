from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="products-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path("ordered_by_price", views.ordered_by_price, name="ordered_by_price"),
    path("ordered_by_name", views.ordered_by_name, name="ordered_by_name"),
    path("nintendo", views.get_nintendo_products, name="get_nintendo_products"),
    path("gameboy", views.get_gameboy_products, name="get_gameboy_products"),
    path("playstation", views.get_playstation_products, name="get_playstation_products"),
    path("xbox", views.get_xbox_products, name="get_xbox_products"),
    path("games", views.get_all_games, name="get_all_games"),
    path("computers", views.get_all_computers, name="get_all_computers")

]
