from django.db import models
from django.contrib.auth.models import User


class Taskmodel(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return self.task_name
