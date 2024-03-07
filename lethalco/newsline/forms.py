from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Post


class PostForm(forms.ModelForm):
    pclasses = [('R', 'Runner'), ('M', 'Monitor')]
    pclass = forms.ChoiceField(choices=pclasses, widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ['title', 'text', 'pclass', ]