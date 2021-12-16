from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.EmailField(unique = True)
    name = models.TextField(max_length = 255)
    password = models.TextField(max_length =255)