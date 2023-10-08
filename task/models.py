from django.db import models

# Create your models here.


class Users(models.Model):
    # user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Profiles(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    nick = models.CharField(max_length=10)
    # image = models.ImageField(default='default.jpg', upload_to='pictures')
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nick


class ToDoLists(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    list_id = models.ForeignKey(ToDoLists, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField()
    #Zmienić na oddzielną tabelkę statusów
    status = models.TextField(Status.name)
    finished = models.BooleanField(null=True)

    #wiedzieć kto i o której dodał
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

