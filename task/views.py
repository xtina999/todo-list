from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task.forms import TaskForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
        model = Tag


class TagCreateView(generic.CreateView):
        model = Tag
        fields = "__all__"
        success_url = reverse_lazy("task:tag-list")
        template_name = "task/tag_form.html"


class TagUpdateView(generic.UpdateView):
        model = Tag
        fields = "__all__"
        success_url = reverse_lazy("task:tag-list")
        template_name = "task/tag_form.html"


class TagDeleteView(generic.DeleteView):
        model = Tag
        template_name = "task/tag_confirm_delete.html"
        success_url = reverse_lazy("task:tag-list")


class TaskCreateView(generic.CreateView):
        model = Task
        form_class = TaskForm
        success_url = reverse_lazy("task:task-list")
        template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
        model = Task
        form_class = TaskForm
        success_url = reverse_lazy("task:task-list")
        template_name = "task/task_form.html"


class TaskDeleteView(generic.DeleteView):
        model = Task
        template_name = "task/task_confirm_delete.html"
        success_url = reverse_lazy("task:task-list")


class TaskCompleteView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return redirect("task:task-list")


class TaskUndoView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_completed = False
        task.save()
        return redirect("task:task-list")
