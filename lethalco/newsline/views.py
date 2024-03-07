from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
import pytz
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .filters import PostFilter
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

class PostsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/posts/')


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'

    # def get_object(self, *args, **kwargs):
    #     obj = cache.get(f'post-{self.kwargs["pk"]}', None)
    #     if not obj:
    #         obj = super().get_object(queryset=self.queryset)
    #         cache.set(f'post-{self.kwargs["pk"]}', obj)
    #     return obj


class PostSearch(ListView):
    model = Post
    ordering = '-date'
    template_name = 'post/search/post_search.html'
    context_object_name = 'post_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    permission_required = ('post.add_post', )

    def form_valid(self, form):
        post = form.save(commit=False)
        form = PostForm(initial={'user_id': self.request.user.id})
        if '/found/' in self.request.path:
            type_ = 'FO'
        elif '/memes/' in self.request.path:
            type_ = 'ME'
        post.type = type_
        post.save()
        return super().form_valid(form)
        