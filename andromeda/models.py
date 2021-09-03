from django.db import models

# Create your models here.
class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='andromeda/img_banner', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    foto = models.ImageField(upload_to='andromeda/img_producto', blank=True, null=True)    

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='andromeda/img_galeria', blank=True, null=True)    

    def __str__(self):
        return self.nombre