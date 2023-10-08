from django.db import models

# Create your models here.


class Task(models.Model):
    ###dołożyć klucz obcy ###
    name = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField()
    #Zmienić na oddzielną tabelkę statusów
    status = models.CharField(max_length=32)
    finished = models.BooleanField(null=True)

    #wiedzieć kto i o której dodał
    added = models.DateTimeField(auto_now_add=True)

