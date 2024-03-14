from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
import pytz
from django.urls import reverse
from .models import Post, User, Message
from .forms import PostForm, MessageForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .filters import PostFilter, MessageFilter
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
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


class PostDelete(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')


class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post/post_create.html'
    permission_required = ('post.change_post', )


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
    template_name = 'post/post_create.html'
    permission_required = ('post.add_post', )

    def form_valid(self, form):
        post = form.save(commit=False)
        if '/found/' in self.request.path:
            type_ = 'FO'
        elif '/memes/' in self.request.path:
            type_ = 'ME'
        post.type = type_
        post.user_id = self.request.user.id
        post.save()
        return super().form_valid(form)


class ProfileDetail(DetailView):
    model = User
    template_name = 'profile/profile.html'
    context_object_name = 'profile'


class ProfileUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = User
    template_name = 'profile/profile_edit.html'
    permission_required = ('profile.change_profile', )


class MessageCreate(PermissionRequiredMixin, CreateView):
    model = Message
    template_name = 'message/message.html'
    form_class = MessageForm
    permission_required = ('message.add_message', )
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.sender_id = self.request.user.id
        post.to = self.kwargs['pk']
        post.save()
        return super().form_valid(form)


class MessageList(ListView):
    model = Message
    template_name = 'message/message_list.html'
    context_object_name = 'messages'
    ordering = '-date'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        self.filterset = MessageFilter(self.request.GET, queryset)
        return self.model.objects.filter(to=self.request.user.id)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class MessageDetail(DetailView):
    model = Message
    template_name = 'message/message_detail.html'
    context_object_name = 'message'

    
def accept_message(request, pk):
    message = Message.objects.get(id=pk)
    message.accept = True
    message.save()
    text = 'Вы успешно подтвердили отклик'
    return render(request, 'message/message_conf.html', {'message': text})



class MessageDelete(PermissionRequiredMixin, DeleteView):
    model = Message
    template_name = 'message/message_delete.html'
    success_url = reverse_lazy('messages')

