from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Taskmodel


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class Taskform(forms.ModelForm):
    class Meta:
        model = Taskmodel
        fields = ["task_name", "task_description"]
