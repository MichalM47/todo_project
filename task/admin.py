from django.contrib import admin
from task.models import Task, ToDoList, Status
from account.models import Profile

# admin.site.register(User)
admin.site.register(ToDoList)
admin.site.register(Task)
# admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Profile)


# Register your models here.
