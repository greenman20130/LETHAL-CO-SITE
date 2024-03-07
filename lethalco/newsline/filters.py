from django_filters import FilterSet
from django.forms import DateInput
from .models import Post
from django import forms
import django_filters


class PostFilter(FilterSet):
    title = django_filters.Filter(
        field_name='title', lookup_expr='icontains', label='Название')
    time = django_filters.DateFilter(
        field_name='time', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}), label='С')
    category = django_filters.Filter(field_name='pclass', lookup_expr='icontains', label='Класс')
    user = django_filters.Filter(
        field_name='user_id', lookup_expr='icontains', label='Автор')
    text = django_filters.Filter(
        field_name='text', lookup_expr='icontains', label='Содержание')

    class Meta:
        model = Post
        fields = {
            'pclass',
            'user_id',
            'title',
            'time',
            'text',
        }