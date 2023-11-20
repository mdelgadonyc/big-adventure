from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("logoff", views.logoff, name="logoff"),
]