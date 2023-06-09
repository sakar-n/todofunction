from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

urlpatterns = [
    path("home/", views.homePage, name="homepage"),
    path("register/", views.registration, name="Registration"),
    path("", views.loginpage, name="login"),
    path("inside/", views.inside, name="inside"),
    path("logout/", views.logoutUser, name="logout"),
    path("taskname", login_required(views.taskname), name="taskname"),
    path("taskedit/<int:task_id>/", login_required(views.taskedit), name="taskedit"),
    path(
        "taskdelete/<int:id>/<str:user>/",
        login_required(views.taskdelete),
        name="taskdelete",
    ),
    path("taskview/", login_required(views.taskview), name="taskview"),
    path("todotask/", login_required(views.todotask), name="todotask"),
    path("taskdetail/<int:id>/", login_required(views.taskdetail), name="taskdetail"),
    path("taskcreate/", login_required(views.taskcreate), name="taskcreate"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
