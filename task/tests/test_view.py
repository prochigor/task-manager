from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task.models import Task, TaskType, Position


class ViewPublicTest(TestCase):
    def setUp(self):
        self.deadline = datetime.now() + timedelta(days=1)
        self.position = Position.objects.create(name="Manager")
        self.type = TaskType.objects.create(name="QA")
        self.worker = get_user_model().objects.create_user(
            username="testuser",
            password="testpass12",
        )
        self.task = Task.objects.create(
            name="Test",
            description="Make test",
            deadline=self.deadline,
            priority="2",
            task_type=self.type,
        )

    def test_task_list_redirect(self):
        url = reverse("task:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_create_redirect(self):
        url = reverse("task:task-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_update_redirect(self):
        url = "/tasks/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_delete_redirect(self):
        url = "/tasks/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_worker_list_redirect(self):
        url = reverse("task:worker-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_worker_create_redirect(self):
        url = reverse("task:worker-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_worker_update_redirect(self):
        url = "/workers/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_worker_delete_redirect(self):
        url = "/workers/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_type_list_redirect(self):
        url = reverse("task:type-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_type_create_redirect(self):
        url = reverse("task:type-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_type_update_redirect(self):
        url = "/types/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_type_delete_redirect(self):
        url = "/types/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_position_list_redirect(self):
        url = reverse("task:position-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_position_create_redirect(self):
        url = reverse("task:position-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_position_update_redirect(self):
        url = "/positions/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_position_delete_redirect(self):
        url = "/positions/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class PrivateViewManagerTest(TestCase):
    def setUp(self):
        self.deadline = datetime.now() + timedelta(days=1)
        self.position = Position.objects.create(name="Manager")
        self.type = TaskType.objects.create(name="Develop")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpassword12", first_name="Bor"
        )
        self.worker.position = self.position
        self.worker.save()
        self.client.force_login(self.worker)
        self.task = Task.objects.create(
            name="Test",
            description="Make test",
            deadline=self.deadline,
            priority="2",
            task_type=self.type,
        )

    def test_content_in_task_list(self):
        url = reverse("task:index")
        response = self.client.get(url)
        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.id)
        self.assertContains(response, self.task.task_type.name)
        self.assertContains(response, "Deadline")
        self.assertContains(response, self.task.priority)

    def test_task_list_view(self):
        url = reverse("task:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_create_page(self):
        url = reverse("task:task-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        Task.objects.create(
            name="Test",
            description="Make test",
            deadline=self.deadline,
            priority="2",
            task_type=self.type,
        )
        task = Task.objects.count()
        self.assertEqual(task, 2)

    def test_task_open_update_page(self):
        url = "/tasks/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_delete(self):
        url = "/tasks/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete task")
        Task.objects.filter(id=self.task.id).delete()
        tasks = Task.objects.count()
        self.assertEqual(tasks, 0)

    def test_content_worker_list(self):
        url = reverse("task:worker-list")
        response = self.client.get(url)
        self.assertContains(response, self.worker.id)
        self.assertContains(response, self.worker.username)
        self.assertContains(response, self.worker.position.name)
        self.assertContains(response, self.worker.tasks.count())
        self.assertContains(response, self.worker.first_name)
        self.assertContains(response, self.worker.last_name)

    def test_content_worker_detail(self):
        response = self.client.get("/workers/1/update/")
        self.assertContains(response, self.worker.username)
        self.assertContains(response, self.worker.position.name)
        self.assertContains(response, self.worker.tasks.count())
        self.assertContains(response, self.worker.first_name)
        self.assertContains(response, self.worker.last_name)

    def test_worker_list_view(self):
        url = reverse("task:worker-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_worker_create_page(self):
        url = reverse("task:worker-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        workers = Task.objects.count()
        self.assertEqual(workers, 1)

    def test_worker_open_update_page(self):
        url = "/workers/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_worker_delete(self):
        url = "/workers/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete worker")
        get_user_model().objects.filter(id=self.task.id).delete()
        workers = get_user_model().objects.count()
        self.assertEqual(workers, 0)

    def test_content_type_list(self):
        url = reverse("task:type-list")
        response = self.client.get(url)
        self.assertContains(response, self.type.id)
        self.assertContains(response, self.type.name)

    def test_type_list_view(self):
        url = reverse("task:type-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_create_page(self):
        url = reverse("task:type-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        workers = Task.objects.count()
        self.assertEqual(workers, 1)

    def test_type_open_update_page(self):
        url = "/types/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_delete(self):
        url = "/types/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete task type")
        TaskType.objects.filter(id=self.task.id).delete()
        types = TaskType.objects.count()
        self.assertEqual(types, 0)

    def test_content_position_list(self):
        url = reverse("task:position-list")
        response = self.client.get(url)
        self.assertContains(response, self.position.id)
        self.assertContains(response, self.position.name)

    def test_position_list_view(self):
        url = reverse("task:position-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_position_create_page(self):
        url = reverse("task:position-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        workers = Task.objects.count()
        self.assertEqual(workers, 1)

    def test_position_open_update_page(self):
        url = "/positions/1/update/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_position_delete(self):
        url = "/positions/1/delete/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete position")
        Position.objects.filter(id=self.position.id).delete()
        positions = Position.objects.count()
        self.assertEqual(positions, 0)
