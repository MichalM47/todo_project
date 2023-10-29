from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView
from task.models import (ToDoList, Task, Status)
from task.forms import ListForm,ListForm2


class ToDoListTemplateView(TemplateView):
    template_name = 'todo_list.html'
    extra_context = {'todolist': ToDoList.objects.all()}


class MainTemplateView(TemplateView):
    template_name = 'main.html'


class TasksListView(View):

    @staticmethod
    def get(request, list_id):
        tasks_list = Task.objects.filter(list_id_id=list_id).values_list('id','name','status')
        # print(tasks_list)

        # return HttpResponse(f'Hello {str(tasks_list)}')
        return render(request, template_name='task.html', context={'tasks':tasks_list})


class DetailListView(View):

    @staticmethod
    def get(request, task_id):
        details_list = Task.objects.filter(id=task_id).values_list('name','status', 'deadline', 'added', 'description')
        status = Status.objects.all().values_list('id','name')

        return render(request, template_name='task_details.html', context={'details':details_list, 'stat':status})


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
        return result


class TaskCreateView(FormView):

    template_name = 'form_task.html'
    form_class = ListForm2
    success_url = reverse_lazy('list')

    def get_form_kwargs(self):

        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Task.objects.create(
            name=cleaned_data['name'],
            list_id=cleaned_data['list_id'],
            description=cleaned_data['description'],
            deadline=cleaned_data['deadline'],
            status=cleaned_data['status'],
            # added=cleaned_data['added'],
            )
        return result


class TaskDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = Task
    success_url = reverse_lazy('list')


class ListDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = ToDoList
    success_url = reverse_lazy('list')


class TaskUpdateView(UpdateView):
    template_name = 'form_task.html'
    model = Task
    form_class = ListForm2
    success_url = reverse_lazy('list')

    def get_form_kwargs(self):

        kwargs = super(TaskUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs




