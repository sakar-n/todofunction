# Generated by Django 4.2 on 2023-04-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="task_description",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="taskmodel",
            name="task_list",
            field=models.CharField(max_length=200),
        ),
    ]
