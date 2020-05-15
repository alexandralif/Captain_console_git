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
    path('computers/', views.get_all_computers, name="get_all_computers"),
    path("order_games_by_name", views.order_games_by_name, name="order_games_by_name"),
    path("order_games_by_price", views.order_games_by_price, name="order_games_by_price"),
    path("nintendo_games", views.get_nintendo_games, name="get_nintendo_games"),
    path("gameboy_games", views.get_gameboy_games, name="get_gameboy_games"),
    path("playstation_games", views.get_playstation_games, name="get_playstation_games"),
    path("xbox_games", views.get_xbox_games, name="get_xbox_games"),
    path("order_nintendo_by_name", views.order_nintendo_by_name, name="order_nintendo_by_name"),
    path("order_nintendo_by_price", views.order_nintendo_by_price, name="order_nintendo_by_price"),
    path("order_gameboy_by_name", views.order_gameboy_by_name, name="order_gameboy_by_name"),
    path("order_gameboy_by_price", views.order_gameboy_by_price, name="order_gameboy_by_price"),
    path("order_playstation_by_name", views.order_playstation_by_name, name="order_playstation_by_name"),
    path("order_playstation_by_price", views.order_playstation_by_price, name="order_playstation_by_price"),
    path("order_xbox_by_name", views.order_xbox_by_name, name="order_xbox_by_name"),
    path("order_xbox_by_price", views.order_xbox_by_price, name="order_xbox_by_price"),
    path("order_computers_by_name", views.order_computers_by_name, name="order_computers_by_name"),
    path("order_computers_by_price", views.order_computers_by_price, name="order_computers_by_price"),

]
