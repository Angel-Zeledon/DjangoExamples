from django.db import models
from login.models import Usuario

class Publicacion(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.TextField(max_length=100)
    miniature = models.ImageField(upload_to='publicaciones/images/', default = 'default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
