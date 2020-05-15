from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="SearchHistory-index"),
    path('clear_search_history/',views.clear_search_history,name="clear_search_history")
]