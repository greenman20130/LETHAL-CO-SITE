from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    text = RichTextUploadingField(null=True)

    meme = 'ME'
    found = 'FO'
    types = [
        (meme, 'Мемы'),
        (found, 'Поиск команды')
    ]
    type = models.CharField(max_length = 13, choices = types, null = True)

    runner = 'R'
    monitor = 'M'
    pclasses = [
        (runner, 'Бегун'),
        (monitor, 'Мониторщик')
    ]
    pclass = models.CharField(max_length = 10, choices = pclasses)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    sender = models.ForeignKey(User, on_delete = models.CASCADE)
    to = models.IntegerField()