from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class Taskform():
    class Meta:
        model = User
        fields = ["title", "description", "complete"]
