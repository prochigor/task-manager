import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name="workers", null=True
    )

    def __str__(self) -> str:
        return (
            f"{self.username} ({self.first_name} {self.last_name}) " f"{self.position}"
        )


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("1", "Deferred"),
        ("2", "Low"),
        ("3", "Medium"),
        ("4", "High"),
        ("5", "Urgent"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, related_name="tasks"
    )
    assignees = models.ManyToManyField(Worker, related_name="tasks", default=None)

    class Meta:
        ordering = (
            "is_completed",
            "-priority",
        )

    def __str__(self) -> str:
        if self.is_completed:
            status = "completed"
        else:
            status = "in progress"
        return (
            f"{self.name}, type: {self.task_type.name}, "
            f"priority: {self.priority}, status: {status}"
        )

    def check_deadline(self):
        return self.deadline > datetime.datetime.now()
