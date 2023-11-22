from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/index.html"
    paginate_by = 8


class TaskDetailView(generic.DetailView):
    model = Task
    paginate_by = 8


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type")
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:index")
