from django.contrib import admin
from task.models import Task, ToDoList, Status


admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Status)




