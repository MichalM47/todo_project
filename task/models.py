from django.db import models
from account.models import Profile, User

# Create your models here.


# class User(models.Model):
#     # user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'


# class Profile(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     nick = models.CharField(max_length=10)
#     image = models.ImageField(default='default.jpg', upload_to='pictures')
#     email = models.EmailField(max_length=254)
#
#     def __str__(self):
#         return self.nick


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

