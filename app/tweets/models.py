from django.db import models
from login.models import Usuario


class Tweet(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE)