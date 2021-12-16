from typing import Optional
from django.db import models as m
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class Servicio(m.Model):
    titulo=m.CharField(max_length=50)
    contenido=m.CharField(max_length=100)
    imagen=m.ImageField(upload_to='servicios') #con este metodo se puede cargar las fotos a la carpeta en media
    costo=m.IntegerField()
    created=m.DateTimeField(auto_now_add=True)
    updated=m.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo