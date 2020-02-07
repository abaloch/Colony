from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=140, blank=True)
    locations = models.CharField(max_length=30, blank=True)
    bday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
