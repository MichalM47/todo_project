from django.urls import path
from .views import ToDoListTemplateView



urlpatterns = [
    path('list/', ToDoListTemplateView.as_view(), name='list'),
    ]
