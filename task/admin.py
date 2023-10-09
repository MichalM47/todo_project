from django.contrib import admin
from task.models import Task, User, ToDoList, Profile, Status

admin.site.register(User)
admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Status)


# Register your models here.
