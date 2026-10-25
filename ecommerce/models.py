from django.contrib.auth.models import User
from django.db import models

CATEGORIAS = [
    ('Anime y manga', 'Anime y manga'),
    ('Streetwear', 'Streetwear'),
]


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='Streetwear')
    imagen = models.CharField(max_length=100, blank=True)
    stock = models.PositiveIntegerField(default=10)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.username
