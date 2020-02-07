from django.urls import path

from . import views

app_name = 'microblog'
urlpatterns = [
    path('', views.FeedView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
