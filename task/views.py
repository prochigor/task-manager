from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from task.forms import (
    WorkerCreationForm,
    TaskCreateForm,
    TaskSearchForm, WorkerSearchForm, TypeSearchForm,
)
from task.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    template_name = "task/index.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    # fields = ("name", "description", "deadline", "priority", "task_type")
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
    paginate_by = 10
    template_name = "task/worker_list.html"
    success_url = reverse_lazy("task:worker-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["name"]
            )
        return queryset


class WorkerCreateView(generic.CreateView):
    model = get_user_model()
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("task:worker-list")


class WorkerDetailView(generic.DetailView):
    model = get_user_model()


class TypeListView(generic.ListView):
    paginate_by = 3
    queryset = TaskType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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
