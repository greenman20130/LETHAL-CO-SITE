from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)
    pclasses = [('R', 'Runner'), ('M', 'Monitor')]
    pclass = forms.ChoiceField(choices=pclasses, widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = '__all__'