from django.contrib import admin
from task.models import Task, Users, ToDoLists, Profiles, Status

admin.site.register(Users)
admin.site.register(ToDoLists)
admin.site.register(Task)
admin.site.register(Profiles)
admin.site.register(Status)


# Register your models here.
