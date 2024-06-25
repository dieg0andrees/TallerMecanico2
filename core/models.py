from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length = 50)

    def __str__(self):
        return self.descripcion

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length = 50,default=True)
    descripcion = models.CharField(max_length = 100,default=True)
    precio = models.CharField(max_length = 15, null=True)
    def __str__(self):
      return self.nombre_servicio
    

class Empleado(models.Model):
    rut = models.CharField(max_length = 12)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length = 60)
    telefono = models.CharField(max_length = 15)
    habilitado = models.BooleanField(default=True)
    genero = models.CharField(max_length = 10, choices=[('masculino','Masculino'),('femenino','Femenino')])
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(TipoEmpleado,on_delete=models.CASCADE)
    servi = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    rut_cliente = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    celular = models.CharField(max_length=15)
    edad = models.IntegerField()
    patente = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rut_cliente})'

class Mecanico_servicio(models.Model):
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    patente_vehiculo = models.CharField(max_length = 10)
    fecha_servicio = models.DateTimeField(auto_now_add=True)
    comentarios = models.CharField(max_length = 500)
    
    def __str__(self):
        return (f"Servicio: {self.servicio.nombre_servicio} - "
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido} - "
                f"Mecánico: {self.mecanico.nombre} {self.mecanico.apellido} - "
                f"Patente: {self.patente_vehiculo} - "
                f"Fecha: {self.fecha_servicio} - "
                f"Precio: {self.servicio.precio}")
