# Generated by Django 4.2.3 on 2023-07-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0002_remove_task_tags_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]