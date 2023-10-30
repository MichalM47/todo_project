from django.test import TestCase, Client
from django.urls import reverse
from task.models import ToDoList
from django.contrib.auth import get_user_model

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        self.task_list = reverse('tasks_list', args=str(2))

    def test_tasks_list_view_GET(self):
        client = Client()

        response = client.get(self.task_list)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'task.html')

    def test_list_create_view(self):

        project= ToDoList.objects.create(
            name='lista'
        )
        project2= ToDoList.objects.create(
            name='lista2'
        )
        self.assertEquals(project.name, 'lista')
        self.assertEquals(project.id, 1)
        self.assertEquals(project2.name, 'lista2')
        self.assertEquals(project2.id, 2)



