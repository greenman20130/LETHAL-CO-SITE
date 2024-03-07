from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    steam_id = models.TextField()

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length = 30)
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    text = models.TextField()
    like = models.IntegerField(default = 0)

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


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE)
    to = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)