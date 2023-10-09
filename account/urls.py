from django.urls import path, include
from .views import LoginViewCustom, SignUpView


urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('sign-up/', SignUpView.as_view(), name='sign_up')

]