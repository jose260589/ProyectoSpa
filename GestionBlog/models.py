from django.db import models as m
from django.contrib.auth.models import User

#from Zoe_Beauty_Spa.GestionServiciosSPA import models

# Create your models here.

class Categoria(m.Model):
    nombre=m.CharField(max_length=50)
    created=m.DateTimeField(auto_now_add=True)
    updated=m.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(m.Model):
    titulo=m.CharField(max_length=50)
    contenido=m.CharField(max_length=100)
    imagen=m.ImageField(upload_to='blog', null=True, blank=True) #con este metodo se puede cargar las fotos a la carpeta en media
    autor=m.ForeignKey(User, on_delete=m.CASCADE)
    created=m.DateTimeField(auto_now_add=True)
    updated=m.DateTimeField(auto_now_add=True)
    categorias=m.ManyToManyField(Categoria)
    class Meta():
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo