from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ToDoList


class ToDoListTemplateView(TemplateView):
    template_name = 'todo_list.html'
    extra_context = {'todolist': ToDoList.objects.all()}