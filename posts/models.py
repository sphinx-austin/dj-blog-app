from django.db import models

# third party import
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title  = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)