# Generated by Django 4.2 on 2023-04-27 05:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskmodel",
            old_name="task_list",
            new_name="task_name",
        ),
    ]