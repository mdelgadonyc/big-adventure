from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from psycopg.errors import UniqueViolation


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world!")


def register(request):
    if request.method == "POST":
        form_data = request.POST
        username = form_data['username']
        email = form_data['email']
        password = form_data['password']
        print(f"Username: {username}\nEmail: {email}\nPassword: {password}\n")
        try:
            user = User.objects.create_user(username=username, email=email, password=email)
            user.set_password(password)
            user.save()
            login(request, user)
            return HttpResponse("Thanks for registering!")
        except (UniqueViolation, IntegrityError):
            messages.error(request, "This account already exist.")
            return redirect('register')

    return render(request, 'register.html')
    # return HttpResponse("Hello, world!")


def signin(request):
    if request.method == "POST":
        form_data = request.POST
        username = form_data['username']
        password = form_data['password']
        print(f"Username: {username}\nPassword: {password}\n")

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('index')

    return HttpResponse("Trying to signin I see.")


def logoff(request):
    if request.user.is_authenticated:
        print("user was signed in, signing out now...")
        logout(request)

    return redirect('index')
