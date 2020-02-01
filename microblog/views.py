from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views import generic

# Create your views here.
class FeedView(generic.ListView):
    template_name = 'microblog/feed.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'microblog/detail.html'
