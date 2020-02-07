import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_text

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Reply(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.reply_text
