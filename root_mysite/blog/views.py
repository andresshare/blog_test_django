from django.shorcuts import render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import Login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView.CreateView,
                                    UpdateView,DeleteView)

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView( LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, List):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_date_isnull=True).order_by('created_date')
