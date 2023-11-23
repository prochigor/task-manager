from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/index.html"
    paginate_by = 8
    queryset = Task.objects.prefetch_related("assignees")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type")
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:index")


class WorkerListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "task/worker_list.html"
    queryset = Worker.objects.select_related("position")
    success_url = reverse_lazy("task:worker-list")


class WorkerCreateView(generic.CreateView):
    model = get_user_model()
    fields = (
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "position",
    )
    success_url = reverse_lazy("task:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = get_user_model()
    fields = (
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "position",
    )
    success_url = reverse_lazy("task:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("task:worker-list")


class WorkerDetailView(generic.DetailView):
    model = get_user_model()


class TypeListView(generic.ListView):
    paginate_by = 3
    queryset = TaskType.objects.all()


class TypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task:type-list")


class TypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task:type-list")


class TypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task:type-list")


class PositionListView(generic.ListView):
    paginate_by = 3
    queryset = Position.objects.all()


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task:position-list")
