from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Post


class PostForm(forms.ModelForm):
    user_id = forms.IntegerField()
    pclasses = [('Runner', 'R'), ('Monitor', 'M')]
    pclass = forms.ChoiceField(choices=pclasses, widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ['title', 'text', 'user_id', 'pclass', ]