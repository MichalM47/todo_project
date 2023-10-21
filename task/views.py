from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import TemplateView
from task.models import (ToDoList, Task)


class ToDoListTemplateView(TemplateView):
    template_name = 'todo_list.html'
    extra_context = {'todolist': ToDoList.objects.all()}


# class TasksTemplateView(TemplateView):
#     template_name = 'task.html'
#     extra_context = {'taskslist': Task.objects.all()}


class DetailsTemplateView(TemplateView):
    template_name = 'task_details.html'
    extra_context = {'details': Task.objects.all()}


class MainTemplateView(TemplateView):
    template_name = 'main.html'


# class TasksListView(View):
#
#     def get(self, request, list_id):
#         to_do_list = ToDoList.objects.filter(id=list_id)
#
#         return HttpResponse(str(to_do_list))

class TasksListView(View):

    def get(self, request, list_id):
        tasks_list = Task.objects.filter(list_id_id=list_id).values_list('name')
        print(tasks_list)

        # return HttpResponse(f'Hello {str(tasks_list)}')
        return render(request, template_name='task.html', context={'tasks':tasks_list})


# class TasksListView(View):
#
#     def get(self, request, list_id):
#         tasks_list = list(Task.objects.filter(list_id_id=list_id).values_list('name'))
#
#         # return HttpResponse(f'Hello {str(tasks_list)}')
#         return render(request, template_name='task.html', context={'tasks':tasks_list})



