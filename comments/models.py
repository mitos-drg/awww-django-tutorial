import datetime

from django.db import models
from django.utils import timezone

class Comment(models.Model):
    text = models.CharField(max_length = 512)
    author = models.CharField(max_length = 64)
    date_created = models.DateTimeField(auto_now = True)
    date_published = models.DateTimeField(default = timezone.now)
