from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Chats(models.Model):
    message = models.ManyToManyField(
        "message_detail.Message", blank = True
    )
    owner = models.ManyToManyField("jwt_auth.User")

    def __str__(self):
        return f"message: {self.message} owner: {self.owner}"
