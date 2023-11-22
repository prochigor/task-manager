from django.shortcuts import render
from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/index.html"
    paginate_by = 8
