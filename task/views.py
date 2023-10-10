from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ToDoList, Task


class ToDoListTemplateView(TemplateView):
    template_name = 'todo_list.html'
    extra_context = {'todolist': ToDoList.objects.all()}


class TasksTemplateView(TemplateView):
    template_name = 'task.html'
    extra_context = {'taskslist': Task.objects.all()}


class DetailsTemplateView(TemplateView):
    template_name = 'task_details.html'
    extra_context = {'details': Task.objects.all()}


