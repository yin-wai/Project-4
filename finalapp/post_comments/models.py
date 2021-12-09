from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class PostReply(models.Model):
    message_sent = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey("jwt_auth.User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "posts.Post", related_name="posts", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.message_sent
