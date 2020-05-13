from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .import views

urlpatterns = [
    path("register",views.register,name="register"),
    path('login',LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('my_account',LoginView.as_view(template_name='user/my_account.html'),name='my_account'),
    #path('create_user', LoginView.as_view(template_name='user/create_user.html'), name="create_user")
    path('create_user', views.create_user, name="create_user")
]

