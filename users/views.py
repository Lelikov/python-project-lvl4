from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def index(request):
    return render(request, 'users/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username, email, password)
    return HttpResponseRedirect('/')