from django.db import models

class Curso(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    descripcion=models.TextField(max_length=50,verbose_name='Descripcion',null=True)
    def __str__(self):
        return "El titulo  :{}  - La descripcion  : {}.".format(self.titulo,self.descripcion)
    #Para borrar tambien la imagen de la base de datos
    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
