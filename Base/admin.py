from django.contrib import admin
from Base.models import Taskmodel

# Register your models here.


class Taskadmin(admin.ModelAdmin):
    list_display = ["task_name", "task_description", "complete", "user"]
    search_fields = ["task_name"]
    list_per_page = 8


admin.site.register(Taskmodel, Taskadmin)
