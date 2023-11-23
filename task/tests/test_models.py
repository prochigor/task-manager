from django.contrib.auth import get_user_model
from django.test import TestCase
from datetime import datetime, timedelta

from task.models import Task, TaskType, Position


class ModelsStrTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(
            name="Manager",
        )
        self.type = TaskType.objects.create(name="Managment")
        self.user = get_user_model().objects.create_user(
            username="testuser",
            first_name="Bob",
            last_name="Mob",
            password="Test19morn",
            position=self.position
        )
        self.task = Task.objects.create(
            name="Test",
            description="Make test",
            deadline=datetime.now() + timedelta(days=1),
            priority="2",
            task_type=self.type,
        )
        # self.user.


    def test_models_str(self):
        self.assertEquals(str(self.position), f"{self.position.name}")
        self.assertEqual(str(self.type), f"{self.type.name}")
        self.assertEqual(
            str(self.user),
            (
                f"{self.user.username} ({self.user.first_name} "
                f"{self.user.last_name}) {self.position}"
            )
        )
        self.assertEqual(
            str(self.task),
            (
                f"{self.task.name}, type: {self.task.task_type.name}, "
                f"priority: {self.task.priority}, status: wait workers{self.task.assignees}"
            )
        )

#     def test_driver_license_number(self):
#         data = {
#             "username": "testuser",
#             "first_name": "Bob",
#             "last_name": "Mob",
#             "password": "Test19morn",
#             "license_number": "ABC19764"
#         }
#         self.assertEqual(
#             self.user.username, data["username"]
#         )
#         self.assertEqual(
#             self.user.first_name, data["first_name"]
#         )
#         self.assertEqual(
#             self.user.last_name, data["last_name"]
#         )
#         self.assertEqual(
#             self.user.license_number, data["license_number"]
#         )
#         self.assertTrue(self.user.check_password(data["password"]))
#
#
# class ModelsFieldsTest(TestCase):
#     def setUp(self) -> None:
#         self.manufacturer = Manufacturer.objects.create(
#             name="testname",
#             country="EU"
#         )
#         self.user = get_user_model().objects.create_user(
#             username="testuser",
#             first_name="Bob",
#             last_name="Mob",
#             password="Test19morn",
#             license_number="ABC19764"
#         )
#         self.car = Car.objects.create(
#             model="testmodel",
#             manufacturer=self.manufacturer,
#         )
#
#     def test_manufacturer_fields_max_length(self):
#         max_len_mame = self.manufacturer._meta.get_field("name").max_length
#         max_len_country = self.manufacturer._meta.get_field(
#             "country"
#         ).max_length
#         self.assertEqual(max_len_mame, 255)
#         self.assertEqual(max_len_country, 255)
#
#     def test_car_fields_max_length(self):
#         max_length = self.car._meta.get_field("model").max_length
#         self.assertEqual(max_length, 255)
