from django.db import models

# Create your models here.
class Killer(models.Model):
    nombre = models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    instagram=models.CharField(max_length=30)
    twiter = models.CharField(max_length=30)
    foto =models.ImageField(upload_to='img',blank=True,null=True,verbose_name='foto_usuario')
    
    def __str__(self):
        return self.nombre


