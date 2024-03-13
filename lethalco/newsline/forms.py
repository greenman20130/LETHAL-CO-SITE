from django import forms
from .models import Post, Message, User
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
    

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Ник: ')
    steam_id = forms.CharField(label='Steam_ID: ')
    class Meta:
        model = User
        fields = ['username', 'steam_id', ]