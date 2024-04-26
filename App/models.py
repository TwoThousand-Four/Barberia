from django.db import models

# Create your models here.

#Clase Tipo Servicio
class TipoServicio(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Servicio")
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")
    
    def __str__(self):
        return self.tipo


#Clase Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo = models.ForeignKey(TipoServicio, on_delete=models.PROTECT, verbose_name="Tipo de Servicio")
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='static/img/servicios', verbose_name="Imagen del servicio", null=True)
    precio =  models.IntegerField(verbose_name="Precio")
    
    def __str__(self):
        return self.nombre
    
    #Borrar imagenes desde el admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
         
#Clase Contacto
opciones_consulta = [
    [0, "Reclamo"],
    [1, "Consulta sobre un servicio"],
    [2, "Mensaje positivo"],
    [3, "Sugerencia"],
]

class Contacto (models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")
    tipo_consulta = models.IntegerField(choices=opciones_consulta, verbose_name="Tipo de consulta")
    mensaje = models.TextField(max_length=1000, verbose_name="Mensaje")
    avisos = models.BooleanField(verbose_name="Avisos")
    
    def __str__(self) :
        return self.nombre