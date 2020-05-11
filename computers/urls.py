from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="computers-index"),
    path('<int:id>', views.get_computer_by_id, name="computer_details"),

]
