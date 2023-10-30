from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task.views import ToDoListTemplateView, TasksListView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse("list")
        self.assertEquals(resolve(url).func.view_class, ToDoListTemplateView)

    def test_tasks_list_url_is_resolved(self):
        url = reverse("tasks_list", args=str(4))
        self.assertEquals(resolve(url).func.view_class, TasksListView)





