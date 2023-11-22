from django.urls import path

from task.views import (
    TaskListView,
    TaskDetailView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="car-detail"),
]

app_name = "task"
