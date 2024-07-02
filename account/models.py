from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=10)
    image = models.ImageField(default='pic.jpg', upload_to='profile_pics')
    email = models.EmailField(max_length=254)
    biography = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


