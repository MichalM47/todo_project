from django.db import models
from account.models import Profile, User


class ToDoList(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    list_id = models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    finished = models.BooleanField(null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

