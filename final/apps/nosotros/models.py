from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    cargo = models.TextField(null=False)
    informacion = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='media/nosotros_defecto.png')
    email = models.EmailField(blank=True, null=True)
    
  

    def __str__(self):
        return self.nombre

class Image(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, upload_to='articulo', default='articulo/nosotros_defecto.jpg')

    def delete(self, using = None, keep_parents = False):
        self.image.delete()
        super().delete(using=using, keep_parents=keep_parents)

# Create your models here.
