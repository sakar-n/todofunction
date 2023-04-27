from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.homePage, name="homepage"),
    path("register/", views.registration, name="Registration"),
    path("login/", views.loginpage, name="login"),
    path("inside/", views.inside, name="inside"),
    path("logout/", views.logoutUser, name="logout"),
    path("taskname/", login_required(views.taskname), name="taskname"),
    path("taskedit/<int:task_id>/", login_required(views.taskedit), name="taskedit"),
    path("taskdelete/<int:id>/", login_required(views.taskdelete), name="taskdelete"),
    path("taskview/", login_required(views.taskview), name="taskview"),
    path("todotask/", login_required(views.todotask), name="todotask"),
    path("taskdetail/<int:id>", login_required(views.taskdetail), name="taskdetail"),
]
