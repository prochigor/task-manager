from django.urls import path

from task.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "task"
