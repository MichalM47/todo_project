from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationFormCustom


class LoginViewCustom(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main')


class SignUpView(CreateView):
    template_name = 'create_account.html'
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('login')
