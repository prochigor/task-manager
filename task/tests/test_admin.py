from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime, timedelta

from task.models import Position, TaskType, Task, Worker


class AdminSiteTest(TestCase):
    def setUp(self):
        self.deadline = datetime.now() + timedelta(days=1)
        self.client = Client()
        self.position = Position.objects.create(name="Manager")
        self.type = TaskType.objects.create(name="Develop")
        self.admin_user = Worker.objects.create_superuser(
            username="admintestuser",
            password="admintestpass",
        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword12",
        )
        self.worker.position = self.position
        self.worker.save()
        self.task = Task.objects.create(
            name="Test",
            description="Make test",
            deadline=self.deadline,
            priority="2",
            task_type=self.type,
        )

    def test_user_list_display(self) -> None:
        url = reverse("admin:task_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position.name)

    def test_worker_detail_fieldset(self) -> None:
        url = reverse("admin:task_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)
        self.assertContains(response, self.worker.first_name)
        self.assertContains(response, self.worker.last_name)

    def test_worker_creation_page_fieldset(self) -> None:
        url = reverse("admin:task_worker_add")
        response = self.client.get(url)
        self.assertContains(response, "position")
        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")

    def test_task_list_display(self) -> None:
        url = reverse("admin:task_task_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.priority)
        self.assertContains(response, self.task.task_type)

    def test_task_detail_fieldset(self) -> None:
        url = reverse("admin:task_task_change", args=[self.task.id])
        response = self.client.get(url)
        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.description)
        self.assertContains(response, "Deadline")
        self.assertContains(response, self.task.priority)
        self.assertContains(response, self.task.task_type)

    def test_task_creation_page_fieldset(self) -> None:
        url = reverse("admin:task_task_add")
        response = self.client.get(url)
        self.assertContains(response, "Name")
        self.assertContains(response, "Description")
        self.assertContains(response, "Deadline")
        self.assertContains(response, "Priority")
        self.assertContains(response, "Task type")
        self.assertContains(response, "Assignees")

    def test_task_type_list_display(self) -> None:
        url = reverse("admin:task_tasktype_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.type.name)

    def test_task_type_detail_fieldset(self) -> None:
        url = reverse("admin:task_tasktype_change", args=[self.type.id])
        response = self.client.get(url)
        self.assertContains(response, self.type.name)

    def test_task_type_creation_page_fieldset(self) -> None:
        url = reverse("admin:task_tasktype_add")
        response = self.client.get(url)
        self.assertContains(response, "Name")

    def test_position_list_display(self) -> None:
        url = reverse("admin:task_position_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.position.name)

    def test_position_detail_fieldset(self) -> None:
        url = reverse("admin:task_position_change", args=[self.position.id])
        response = self.client.get(url)
        self.assertContains(response, self.position.name)

    def test_position_creation_page_fieldset(self) -> None:
        url = reverse("admin:task_position_add")
        response = self.client.get(url)
        self.assertContains(response, "Name")
