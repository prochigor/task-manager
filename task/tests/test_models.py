from django.contrib.auth import get_user_model
from django.test import TestCase
from datetime import datetime, timedelta

from task.models import Task, TaskType, Position


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.deadline = datetime.now() + timedelta(days=1)
        self.position = Position.objects.create(
            name="Manager",
        )
        self.type = TaskType.objects.create(name="Managment")
        self.user = get_user_model().objects.create_user(
            username="testuser",
            first_name="Bob",
            last_name="Mob",
            password="Test19morn",
            position=self.position,
        )
        self.task = Task.objects.create(
            name="Test",
            description="Make test",
            deadline=self.deadline,
            priority="2",
            task_type=self.type,
        )

    def test_models_str(self):
        self.assertEquals(str(self.position), f"{self.position.name}")
        self.assertEqual(str(self.type), f"{self.type.name}")
        self.assertEqual(
            str(self.user),
            (
                f"{self.user.username} ({self.user.first_name} "
                f"{self.user.last_name}) {self.position}"
            ),
        )
        self.assertEqual(
            str(self.task),
            (
                f"{self.task.name}, type: {self.task.task_type.name}, "
                f"priority: {self.task.priority}, status: in progress"
            ),
        )

    def test_user_create(self):
        data = {
            "username": "testuser",
            "first_name": "Bob",
            "last_name": "Mob",
            "password": "Test19morn",
            "position": "Manager",
        }
        self.assertEqual(self.user.username, data["username"])
        self.assertEqual(self.user.first_name, data["first_name"])
        self.assertEqual(self.user.last_name, data["last_name"])
        self.assertEqual(self.user.position.name, data["position"])
        self.assertTrue(self.user.check_password(data["password"]))
