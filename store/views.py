from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from psycopg.errors import UniqueViolation


def increase_count(request):
    count = get_count(request)
    if count is None:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return request.session['count']


def get_count(request):
    return request.session.get('count')


def update_cart_count(request):
    if request.method == "POST":
        form_data = request.POST
        print("Django view function update_cart_count has been triggered")
    # response_data = {'message': get_count(request)}
    return HttpResponse(increase_count(request))


# Create your views here.
def index(request):
    context = {'count': get_count(request)}
    return render(request, 'index.html', context)


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

    context = {'count': get_count(request)}
    return render(request, 'register.html', context)


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
