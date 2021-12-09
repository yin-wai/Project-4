from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey("jwt_auth.User", on_delete=models.CASCADE)
    post_comments = models.ManyToManyField(
        "post_comments.PostComments", related_name="postcomments", blank=True)
    def __str__(self):
        return self.text