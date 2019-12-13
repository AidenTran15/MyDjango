

from django.urls import path
from . import views

urlpattern = [
    path("register", views.register, name="register")
]