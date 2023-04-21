from django.shortcuts import render, redirect
from .forms import Signupform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import Taskmodel
from django.contrib.auth.decorators import login_required
from .forms import Taskform
from django.http import HttpResponseRedirect

# Create your views here.


def homePage(request):
    return render(request, "auth_system/home.html")


def registration(request):
    form = Signupform()
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "auth_system/registration.html", {"form": form})


def loginpage(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Email or password is correct")
            return redirect("tasklist")
        else:
            messages.info(request, "Email or password is incorrect")
    return render(request, "auth_system/login.html", {"form": form})


def inside(request):
    return render(request, "auth_system/inside.html")


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required
def tasklist(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/tasklist")
    else:
        form = Taskform
        return render(request, "auth_system/tasklist.html", {"form": form})


@login_required
def taskview(request):
    view_list = Taskmodel.objects.all()
    return render(request, "auth_system/taskview.html", {"view_list": view_list})


@login_required
def taskdelete(request):
    
    pass


@login_required
def taskcreate(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasklist")
    else:
        return render(request, "auth_system/tasklist.html", {"form": form})


@login_required
def taskupdate():
    pass
