from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Taskmodel


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class Taskform(forms.ModelForm):
    task_list = forms.CharField(label="TO DO", max_length=100)
    task_description = forms.CharField(label="Task Discription", max_length=100)

   
    class Meta:
        model = Taskmodel
        fields = ["task_list", "task_description"]