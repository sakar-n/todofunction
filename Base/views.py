from django.shortcuts import render, redirect, get_object_or_404
from .forms import Signupform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import Taskmodel
from django.contrib.auth.decorators import login_required
from .forms import Taskform, Signupform
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def homePage(request):
    
    return render(request, "auth_system/home.html")


def registration(request):
    form = Signupform()
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("User Has been Registered"))
            return redirect('login')
    else:   
        return render(request, "auth_system/registration.html", {"form": form})


def loginpage(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
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
            task =form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, ("Item Has been added"))
            return redirect("tasklist")
    else:
        form = Taskform
        return render(request, "auth_system/tasklist.html", {"form": form})


@login_required
def taskview(request):
    view_list = Taskmodel.objects.filter(user=request.user.id)
    
    return render(request, "auth_system/taskview.html", {'view_list': view_list})


@login_required
def taskdelete(request,id):
    context ={}
    obj = get_object_or_404(Taskmodel, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/taskview")
    
    return render(request, "auth_system/taskdelete.html", context)


    



@login_required
def taskupdate(request,id):
    context ={}
    obj = get_object_or_404(Taskmodel, id = id)
    if request.method == "POST":
        obj.complete
   
   
