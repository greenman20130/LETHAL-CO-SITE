from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import User

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    username = forms.CharField(label = "Ник")
    steam_id = forms.CharField(label = "Steam_id")

    class Meta:
        model = User
        fields = ["username", 
                  "steam_id",
                  "email",
                  "password1", 
                  "password2", ]
        


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
