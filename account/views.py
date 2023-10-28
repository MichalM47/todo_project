from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationFormCustom, ProfileUpdateForm


class LoginViewCustom(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main')


class SignUpView(CreateView):
    template_name = 'create_account.html'
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('login')


def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'profile.html',context)


