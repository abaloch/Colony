from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.
class FeedView(generic.ListView):
    model = Post
    template_name = 'microblog/feed.html'
    context_object_name = 'latest_posts'
    #how the posts are order on the feed
    ordering = ['-pub_date']
    #can paginate easily by adding this attribute
    paginate_by = 5


    # def get_queryset(self):
    #     """Return the last five published posts."""
    #     return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'microblog/detail.html'

#the LoginRequiredMixin makes the share post page only viewable if logged into an account
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['post_text']

    def form_valid(self, form):
        #letting form know that user logged in is the author of post
        form.instance.author = self.request.user
        form.instance.pub_date = timezone.now()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['post_text']

    def form_valid(self, form):
        #letting form know that user logged in is the author of post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        #gets the current post
        post = self.get_object()

        #checking if current logged in user is the same as the post author
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    #this will send user to home page after post is deleted
    success_url = '/'

    def test_func(self):
        #gets the current post
        post = self.get_object()

        #checking if current logged in user is the same as the post author
        if self.request.user == post.author:
            return True
        return False

class UserFeedView(generic.ListView):
    model = Post
    template_name = 'microblog/user_posts.html'
    context_object_name = 'latest_posts'
    #how the posts are order on the feed
    #can paginate easily by adding this attribute
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')
