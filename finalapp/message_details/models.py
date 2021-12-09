from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        "jwt_auth.User", related_name="author", on_delete=models.CASCADE
    )
    sent_to = models.ForeignKey(
        "jwt_auth.User", related_name="sent_to", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text

