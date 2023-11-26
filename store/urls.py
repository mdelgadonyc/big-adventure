from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update-cart-count", views.update_cart_count, name="update_cart_count"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("logoff", views.logoff, name="logoff"),
]
