from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import User
# Register your models here.
from django.contrib.auth import get_user_model
admin.site.register(User)
# Register your models here.
