from django.test import TestCase, Client
from django.urls import reverse, resolve
from task.views import TasksListView


class TestViews(TestCase):

    def setUp(self):
        self.task_list = reverse('tasks_list', args=str(2))

    def test_tasks_list_view_GET(self):
        client = Client()

        response = client.get(self.task_list)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'task.html')



