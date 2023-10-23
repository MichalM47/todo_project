from django.urls import path
from .views import ToDoListTemplateView, DetailListView, MainTemplateView, TasksListView, ListCreateView,TaskCreateView, TaskDeleteView


urlpatterns = [
    path('list/', ToDoListTemplateView.as_view(), name='list'),
    path('tasks/<int:list_id>/', TasksListView.as_view(), name='tasks_list'),
    path('details/<int:task_id>/', DetailListView.as_view(), name='details'),
    path('', MainTemplateView.as_view(), name='main'),
    path('list/create', ListCreateView.as_view(), name='list_create'),
    path('task/create>', TaskCreateView.as_view(), name='task_create'),
    path('task/delete/<pk>', TaskDeleteView.as_view(), name='task_delete'),
    ]
