from django.shortcuts import render, redirect, get_object_or_404
from .forms import Signupform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import Taskmodel
from django.contrib.auth.decorators import login_required, permission_required
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

            return redirect("login")
        else:
            messages.error(request, "User already exist")
            return redirect("Registration")
    return render(request, "auth_system/registration.html", {"form": form})


def loginpage(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("taskname")
        else:
            messages.info(request, "Email or password is incorrect")
    return render(request, "auth_system/login.html", {"form": form})


def inside(request):
    return render(request, "auth_system/inside.html")


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required
def taskname(request):
    if request.method == "POST":
        form = Taskform(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            existing_task_name = Taskmodel.objects.filter(
                user=request.user, task_name=task.task_name
            )
            if existing_task_name.exists():
                messages.error(request, "Task already exists")
            else:
                task.save()

                messages.success(request, ("Item Has been added"))
            return redirect("taskname")
        else:
            messages.error(request, "Task already exist")
            return redirect("taskname")
    else:
        form = Taskform
        Task_name = Taskmodel.objects.filter(user=request.user.id)
        return render(
            request, "auth_system/taskname.html", {"form": form, "Task_name": Task_name}
        )


@login_required
def todotask(request):
    Task_name = Taskmodel.objects.filter(user=request.user.id)

    return render(request, "auth_system/todotask.html", {"Task_name": Task_name})


@login_required
def taskview(request):
    Task_name = Taskmodel.objects.filter(user=request.user.id)

    return render(request, "auth_system/taskview.html", {"Task_name": Task_name})


@login_required
# @permission_required("views.taskdelete", raise_exception=True)
def taskdelete(request, id, user):
    obj = get_object_or_404(Taskmodel, id=id)
    user = request.user.id
    if request.user == obj.user:
        if request.method == "POST":
            obj.delete()
            messages.success(request, ("Item Has been deleted"))
            return HttpResponseRedirect("/todotask")
        return render(request, "auth_system/taskdelete.html", {"task": obj})
    else:
        messages.error(request, "You are not authorized to delete this task.")
        return redirect("todotask")


@login_required
def taskdetail(request, id):
    obj = get_object_or_404(Taskmodel, id=id)
    user_id = obj.user_id

    if request.user.id == obj.user_id:
        context = {
            "task_name": obj.task_name,
            "task_description": obj.task_description,
            "task_id": obj.id,
        }

        return render(request, "auth_system/taskdetail.html", context)
    else:
        messages.error(request, "You are not authorized to view this task.")
        return redirect("taskname")


@login_required
# @permission_required("views.delete_task", raise_exception=True)
def taskedit(request, task_id):
    obj = get_object_or_404(Taskmodel, id=task_id)
    user_id = obj.user_id
    if request.user.id == obj.user_id:
        if request.method == "POST":
            fm = Taskform(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()
                return redirect("taskdetail", id=task_id)
        else:
            fm = Taskform(instance=obj)

            return render(request, "auth_system/taskedit.html", {"form": fm})
    else:
        messages.error(request, "You are not authorized to edit this task.")
        return redirect("taskname")


def home_view(request):
    return render(request, "login.html")
