from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .models import BaseRegisterForm 

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/login'


class BaseLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    success_url = '/posts/'
