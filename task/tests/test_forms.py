from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from task.forms import (
    TaskCreateForm,
    TaskSearchForm,
    WorkerSearchForm,
    TypeSearchForm,
    PositionSearchForm,
)
from task.models import Worker, TaskType, Position


class FormsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.position = Position.objects.create(name="Test Position")
        self.worker = Worker.objects.create(
            username="testworker",
            password="testpassword",
            position=self.position
        )

        self.task_type = TaskType.objects.create(name="Test Type")

    def test_task_create_form(self):
        form_data = {
            "name": "New Task",
            "description": "Task Description",
            "deadline": timezone.now() + timezone.timedelta(days=1),
            "priority": "3",
            "task_type": self.task_type.id,
        }
        form = TaskCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_create_form_with_invalid_deadline(self):
        form_data = {
            "name": "Task",
            "description": "Task Description",
            "deadline": timezone.now() - timezone.timedelta(days=1),
            "priority": "5",
            "task_type": self.task_type.id,
        }
        form = TaskCreateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_search_form(self):
        form_data = {
            "name": "SearchQuery",
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_search_form(self):
        form_data = {
            "name": "SearchQuery",
        }
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_type_search_form(self):
        form_data = {
            "name": "SearchQuery",
        }
        form = TypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_search_form(self):
        form_data = {
            "name": "SearchQuery",
        }
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
