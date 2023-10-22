from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from task.models import (ToDoList, Task, Status)
from task.forms import ListForm


class ToDoListTemplateView(TemplateView):
    template_name = 'todo_list.html'
    extra_context = {'todolist': ToDoList.objects.all()}


# class TasksTemplateView(TemplateView):
#     template_name = 'task.html'
#     extra_context = {'taskslist': Task.objects.all()}


# class DetailsTemplateView(TemplateView):
#     template_name = 'task_details.html'
#     extra_context = {'details': Task.objects.all()}


class MainTemplateView(TemplateView):
    template_name = 'main.html'


# class TasksListView(View):
#
#     def get(self, request, list_id):
#         to_do_list = ToDoList.objects.filter(id=list_id)
#
#         return HttpResponse(str(to_do_list))

class TasksListView(View):

    @staticmethod
    def get(request, list_id):
        tasks_list = Task.objects.filter(list_id_id=list_id).values_list('id','name')
        # print(tasks_list)

        # return HttpResponse(f'Hello {str(tasks_list)}')
        return render(request, template_name='task.html', context={'tasks':tasks_list})


class DetailListView(View):

    @staticmethod
    def get(request, task_id):
        # print("aaa")
        details_list = Task.objects.filter(id=task_id).values_list('description', 'status', 'deadline', 'added')
        status = Status.objects.all().values_list('id','name')

        return render(request, template_name='task_details.html', context={'details':details_list, 'stat':status})
        # return HttpResponse(f'Hello {str(details_list)}')


class ListCreateView(FormView):

    template_name = 'form.html'
    form_class = ListForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        ToDoList.objects.create(
            name=cleaned_data['name'],
            user_id= self.request.user
            )
    #     # Task.objects.create(
    #     #     title=cleaned_data['title'],
    #     #     genre=cleaned_data['genre'],
    #     #     rating=cleaned_data['rating'],
    #     #     released=cleaned_data['released'],
    #     #     description=cleaned_data['description']
    #     # )
        return result

    # def get_form_kwargs(self):
    #     kwargs=super().get_form_kwargs()
    #     user = self.request.user
    #     kwargs["initial"]





