from django.urls import path

from task.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    WorkerDetailView,
    TypeListView,
    TypeCreateView,
    TypeUpdateView,
    TypeDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path("types/", TypeListView.as_view(), name="type-list"),
    path("types/create/", TypeCreateView.as_view(), name="type-create"),
    path(
        "types/<int:pk>/update/",
        TypeUpdateView.as_view(),
        name="type-update"
    ),
    path(
        "types/<int:pk>/delete/",
        TypeDeleteView.as_view(),
        name="type-delete"
    ),
]

app_name = "task"
