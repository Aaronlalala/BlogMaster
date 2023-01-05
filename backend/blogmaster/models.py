from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # Many-to-one relationships: an user could have many posts but a post could only have one user.
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    creation_time = models.DateField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    following = models.ManyToManyField(User, related_name="follower")

class Comment(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    creation_time = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

