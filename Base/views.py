from django.shortcuts import render, redirect
from .forms import Signupform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import Taskform

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
            return redirect("inside")
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
    model_data = User.objects.all()
    return render(request, "auth_system/tasklist.html", {"model_data": model_data})


@login_required
def taskcreate(request):
    pass


@login_required
def taskdelete():
    pass


@login_required
def taskcreate(request):
    form = Taskform()
    model_data = Taskform.objects.all()
    context = {"model_data": model_data}
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "auth_system/tasklist.html", context)

@login_required
def taskupdate():
    pass
