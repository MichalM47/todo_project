from django.contrib import admin
from task.models import Task, Users, ToDoLists

admin.site.register(Users)
admin.site.register(ToDoLists)
admin.site.register(Task)


# Register your models here.
