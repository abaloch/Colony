from django.urls import path
from .views import (
FeedView, DetailView,
PostCreateView, PostUpdateView,
PostDeleteView, UserFeedView
)
from . import views

app_name = 'microblog'
urlpatterns = [
    path('', FeedView.as_view(), name='home'),
    path('user/<str:username>', UserFeedView.as_view(), name='user-posts'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]
