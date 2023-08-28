from django.db import models

# third party import
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title  = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)