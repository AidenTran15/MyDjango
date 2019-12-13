

from django.urls import path
from . import views

urlpattern = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("Logout", views.logout, name="logout")
]