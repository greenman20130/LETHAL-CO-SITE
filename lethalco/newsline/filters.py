from django_filters import FilterSet
from django.forms import DateInput
from .models import Post, Message
from django import forms
import django_filters


class PostFilter(FilterSet):
    title = django_filters.Filter(
        field_name='title', lookup_expr='icontains', label='Название')
    date = django_filters.DateFilter(
        field_name='date', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}), label='С')
    category = django_filters.Filter(field_name='pclass', lookup_expr='icontains', label='Класс')
    user = django_filters.Filter(
        field_name='user_id', lookup_expr='icontains', label='Автор')
    text = django_filters.Filter(
        field_name='text', lookup_expr='icontains', label='Содержание')
    type = django_filters.Filter(
        field_name='type', lookup_expr='icontains', label='Тип')

    class Meta:
        model = Post
        fields = {
            'pclass',
            'user_id',
            'title',
            'date',
            'text',
            'type',
        }


class MessageFilter(FilterSet):
    text = django_filters.Filter(
        field_name='text', lookup_expr='icontains', label='Текст')
    date = django_filters.DateFilter(
        field_name='date', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}), label='С')
    sender_id = django_filters.Filter(
        field_name='sender_id', lookup_expr='icontains', label='От')

    class Meta:
        model = Message
        fields = {
            'text',
            'sender_id',
            'date',
        }