from django.test import Client, RequestFactory, TestCase
from tasks import views
from tasks.models import Task, TaskStatus, Tag
from django.contrib.auth.models import User


class TaskTest(TestCase):

    def setUp(self):
        """Initial"""
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user',
            password='password!@#',
        )
        self.client = Client()

    def createTask(self):
        """Create task"""
        status = TaskStatus.objects.create(name='Status for test')
        tag = Tag.objects.create(name='Tag for test')
        task = Task.objects.create(
            name='Name for test',
            description='Description for test',
            assigned_to=self.user,
            creator=self.user,
            status=status,
        )
        task.tags.add(tag)
        return task

    def test_task_create(self):
        """Test task creation."""
        task = self.createTask()
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task.name)
        self.assertEqual(Task.objects.count(), 1)

    def test_tasks_view(self):
        """Test tasks view"""
        request = self.factory.get('/')
        request.user = self.user
        response = views.TasksViews.as_view()(request)
        self.assertEqual(response.status_code, 200)
