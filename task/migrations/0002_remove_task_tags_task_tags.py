# Generated by Django 4.2.3 on 2023-07-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="tags",
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="tasks", to="task.tag"),
        ),
    ]