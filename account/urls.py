from django.urls import path, include
from .views import LoginViewCustom, SignUpView, profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile,name='profile')

]