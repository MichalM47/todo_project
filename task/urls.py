from django.urls import path
from .views import ToDoListTemplateView, DetailListView, MainTemplateView, TasksListView


urlpatterns = [
    path('list/', ToDoListTemplateView.as_view(), name='list'),
    path('tasks/<int:list_id>/', TasksListView.as_view(), name='tasks_list'),
    path('details/<int:task_id>/', DetailListView.as_view(), name='details'),
    path('', MainTemplateView.as_view(), name='main'),
    ]
