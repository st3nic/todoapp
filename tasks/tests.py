from django.test import TestCase
from tasks.models import Task
from django.contrib.auth.models import User

# Create your tests here.
class TaskTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', password='12345')
        Task.objects.create(task="Task1", priority="HIGH", status="NEW", who=user)


    def test_add_task(self):
        task = Task.objects.get(task="Task1")
        self.assertEqual(task.task, 'Task1')
        self.assertEqual(task.priority, 'HIGH')
        self.assertEqual(task.status, 'NEW')

    def test_update_task(self):
        task = Task.objects.get(task="Task1")
        task.status = 'In Progress'
        task.priority = 'Medium'
        task.save()
        self.assertEqual(task.status, 'In Progress')
        self.assertNotEqual(task.status, 'New')
        self.assertEqual(task.priority, 'Medium')
        self.assertNotEqual(task.priority, 'High')

