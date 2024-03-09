from django import forms
from .models import Post, Message
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(widget=CKEditorUploadingWidget, label='Текст')
    pclasses = [('R', 'Runner'), ('M', 'Monitor')]
    pclass = forms.ChoiceField(choices=pclasses, widget=forms.RadioSelect, label='Кто ты воин')
    class Meta:
        model = Post
        fields = ['title', 'text', 'pclass']


class MessageForm(forms.ModelForm):
    text = forms.CharField(label='Текст сообщения: ')

    class Meta:
        model = Message
        fields = ['text', ]