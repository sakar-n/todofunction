from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.homePage, name="homepage"),
    path("register/", views.registration, name="Registration"),
    path("login/", views.loginpage, name="login"),
    path("inside/", views.inside, name="inside"),
    path("logout/", views.logoutUser, name="logout"),
    path("tasklist/", login_required(views.tasklist), name="tasklist"),
    path("taskcreate/", login_required(views.taskcreate), name="taskcreate"),
    path("taskupdate/<int:pk>/", login_required(views.taskupdate), name="taskupdate"),
    path("taskdelete/<int:pk>/", login_required(views.taskdelete), name="taskdelete"),
]
